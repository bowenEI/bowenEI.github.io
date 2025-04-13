---
# Documentation: https://hugoblox.com/docs/managing-content/

title: "大模型推理技术栈"
subtitle: ""
summary: ""
authors: []
tags: [LLM, Inference]
categories: [Essay, Knowledge]
date: 2024-01-02T18:20:53+08:00
lastmod: 2024-01-19T18:20:53+08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

toc: true
---

持续更新中……

<!--more-->

## 优化技术

```markmap
- 模型压缩
  - Pruning
  - Quantization
- 显存优化
  - [PagedAttention](https://doi.org/10.48550/arXiv.2309.06180)
  - Quantized K/V Cache
  - [Multi Query Attention (MQA)](https://doi.org/10.48550/arXiv.1911.02150)
    - [Grouped Query Attention (GQA)](https://doi.org/10.48550/arXiv.2305.13245)
  - [FlashAttention](https://doi.org/10.48550/arXiv.2205.14135)
    - [FlashAttention-2](https://doi.org/10.48550/arXiv.2307.08691)
    - [Flash-Decoding](https://crfm.stanford.edu/2023/10/12/flashdecoding.html)
    - [FlashDecoding++](https://doi.org/10.48550/arXiv.2311.01282)
- 调度优化
  - [Dynamic Batching](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html#dynamic-batcher)
  - [Async Serving](https://towardsdatascience.com/async-calls-for-chains-with-langchain-3818c16062ed)
  - [Iteration batching (a.k.a. continuous batching)](https://friendli.ai/blog/llm-iteration-batching/)
- 高性能算子
  - Operator Fusion
- 模型编译
  - [XLA](https://www.tensorflow.org/xla?hl=zh-cn)
  - [MLC LLM](https://llm.mlc.ai/)
```

## 框架

```markmap
- 并行训练框架
  - [DeepSpeed](https://github.com/microsoft/DeepSpeed)
  - [Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
  - [Colossal-AI](https://github.com/hpcaitech/ColossalAI)
  - [Alpa](https://www.usenix.org/conference/osdi22/presentation/zheng-lianmin)
  - [GShard](https://doi.org/10.48550/arXiv.2006.16668)
    - [GSPMD](https://doi.org/10.48550/arXiv.2105.04663)
- 推理服务框架
  - [Orca](https://www.usenix.org/conference/osdi22/presentation/yu)
  - [LMDeploy](https://github.com/InternLM/lmdeploy)
  - [LightLLM](https://github.com/ModelTC/lightllm)
- 推理加速框架
  - [vLLM](https://github.com/vllm-project/vllm)
  - [FasterTransformer](https://github.com/NVIDIA/FasterTransformer)
    - [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)
  - [Text Generation Inference](https://github.com/huggingface/text-generation-inference)
  - [Lit-LLaMA](https://github.com/Lightning-AI/lit-llama)
  - [fastllm](https://github.com/ztxz16/fastllm)
  - [InferLLM](https://github.com/MegEngine/InferLLM)
  - [OpenPPL](https://openppl.ai/home)
  - [DeepSpeed-FastGen](https://github.com/microsoft/DeepSpeed/blob/master/blogs/deepspeed-fastgen/chinese/README.md)
  - [ExLlama](https://github.com/turboderp/exllama)
```