---
title: "Serving Large Language Models on Huawei CloudMatrix384"
subtitle: "在华为超节点上部署大模型"
date: 2025-10-03T01:35:10+08:00
draft: true
tags:
- LLM
- 文献精读
---

华为超节点（CloudMatrix384）是华为在 2025 年发布的一种突破了冯·诺伊曼体系结构，将各类异构资源通过 UB（Unified Bus，统一总线）整合而成的超大规模计算节点，专为 LLM（Large Language Model，大语言模型）服务而设计。在此基础上，华为还提出了 CloudMatrix-Infer 推理系统，提出了 PDC（Prefill-Decode-Cache）分离架构、LEP（Large Expert Parallel，大规模专家并行）等创新技术，为大语言模型的高效推理提供了强大支持。

<!--more-->

> [arXiv](https://arxiv.org/abs/2506.12708) 论文链接

## 核心创新点

1. CloudMatrix 超节点架构
    - 通过 UB 互连，使多个节点在逻辑上组成一个整体计算机
2. CloudMatrix-Infer 推理系统
    - 采用 PDC 分离架构，将 prefill、decode 和 caching 三个阶段分离部署
    - 引入 LEP 大规模专家并行技术，有效支持 MoE 模型推理
    - 采用硬件感知量化方案，针对 Ascend 910 硬件特性优化 INT8 量化
3. 突破性性能指标
    - 4K 长度提示词下实现 6688 tok/s[^2]，TPOT 达到 1943 tok/s

[^2]: tok/s: Tokens per second 每秒处理的令牌数

## CloudMatrix 架构详解

### 超节点的设计理念

![](./assets/imgs/Fig1.png "CloudMatrix 超节点的设计理念")

超节点设计的核心思路在于突破传统的冯·诺依曼体系结构，将各类异构资源通过 UB 统一总线整合而成的超大规模计算节点。这些异构资源包括 NPU、NPU、存储、网卡等，它们都是分离式且可扩展的。

关键的核心在于超高带宽且低延迟的 UB，优势在于：

- 消除了节点间的通信瓶颈，特别是对于 LLM（MoE）模型中的 TP 和 EP。
- 所有的异构资源解耦，可根据任务特性（如计算密集型的 prefill 和访存密集型的 decode）调整 CPU/NPU 配比。
- 使多任务负载混合流水线执行，提高资源利用率。
- 存储分离消除传统 I/O 瓶颈，支持高吞吐量的 K/V 缓存存储。

### CloudMatrix384 案例分析

CloudMatrix384 是一种搭载了 384 个 Ascend 910 NPU 和 192 个 Kunpeng CPU 的超节点，每个节点配备 8 个 NPU 和 4 个 CPU。据此可推得一个超节点内共有 48 个节点。

CloudMatrix384 的设计要点是：

- peer-to-peer 点对点通信
- fully interconnected 全互联
- ultra-high-bandwidth 超高带宽

![](./assets/imgs/Fig2.png "CloudMatrix384 超节点的架构")

超节点的三层网络平面：

1. **UB 平面**：实现非阻塞的 NPU/CPU 全互联，支持 TP/EP （超节点内）跨节点和跨设备存储访问
    - 1 级 UB：节点内 NPU/CPU 全互联
    - 2 级 UB：超节点内跨节点 NPU/CPU 全互联
2. **RDMA 平面**：支持跨超节点的 NPU 间通信，传输因 PDC 分离产生的 K/V 缓存
3. **VPC[^1] 平面**：负责上层的部署、调度、管理和监控等功能

[^1]: VPC: Virtual Private Cloud 虚拟私有云

### 硬件组件

![](./assets/imgs/Fig3.png "Ascend 910C 架构")

> 一块 Ascend 910C 芯片由两块 Ascend 910D 组成。

![](./assets/imgs/Fig4.png "CloudMatrix384 超节点内的一个节点")

![](./assets/imgs/Fig5.png "CloudMatrix384 超节点内的 UB 交换系统")

## CloudMatrix-Infer 部署 DeepSeek 模型

### 基于 P2P 的 PDC 分离部署

![](./assets/imgs/Fig9.png "CloudMatrix384 超节点内的 PDC 分离部署架构")

Prefill 集群：

- 每个 P 实例配备 16 块 NPU
- 并行策略：
    - MLA：分阶段混合并行
    - MoE：EP=32，其中每个 rank：
        - 1 个共享专家
        - 8 个路由专家
        - 1 个冗余专家

Decode 集群：

- 每个 D 实例配备 160 块 NPU
- 并行策略：
    - MLA：DP=320
    - MoE：EP=320，每个 rank 包含 1 个专家，共包括：
        - 32 个共享专家
        - 256 个路由专家
        - 32 个冗余专家

此外，MoE 阶段均采用了 [EPLB](https://github.com/deepseek-ai/EPLB)（Expert Parallelism Load Balancer）优化。

> P/D 分离部署的并行策略除 Prefill 的 MLA 外，其余与 [DeepSeek-V3 的技术报告](https://arxiv.org/abs/2412.19437)中所述一致。

可以进一步推得，在一个 CloudMatrix384 超节点内：

- P 实例共有 4 个，需要共计 64 个 NPU
- D 实例共有 2 个，需要共计 320 个 NPU

注意到 P/D 之间的 hidden states 通过 RDMA 平面通信。而 P 节点的 K/V 缓存则通过 UB 存储到远程 C 节点上，D 节点则从 C 节点远程读取之。于是，PDC 三者之间形成生产者-消费者模型。

{{< callout type="note" >}}

**P2P 架构和 K/V 缓存中心化架构对比**

K/V 缓存中心化架构主要由过去一些系统（如 [Nvidia Dynamo](https://github.com/ai-dynamo/dynamo)、[Mooncake](https://github.com/kvcache-ai/Mooncake)）提出和采用。它的最大特点是请求调度与本地 K/V 缓存读写是紧耦合的。这带来的挑战是，节点内访存带宽大大高于节点间通信带宽，因此远程 K/V 缓存访问延迟成为了性能瓶颈。

如果采用 CloudMatrix 所提出的 P2P 架构，它的最大特点是扁平化的，P/D 都可以直接访问。而且，超节点内的通信都是基于 UB 的，因此不存在节点间通信瓶颈。总而言之，其优势在于：

- 轻量级、无状态的调度，不受数据局部性的限制
- 调度机制需求低
- 增加存储器资源利用率

{{< /callout >}}

此外，在长序列任务绘制用户会话异步到达与离开等场景中，负载通常是异步的。为了更好地提高资源利用率，CloudMatrix-Infer 会强制伪同步执行。

### Decode：大规模专家并行

#### MoE 优化：融合通信算子

#### MLA 优化

#### Pipeline & Overlapping

#### MTP 优化

### Prefill：分阶段混合并行

#### MLA 优化

#### Pipeline & Overlapping

#### P/D 低干扰传输
