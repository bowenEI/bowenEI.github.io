---
## Documentation: https://wowchemy.com/docs/managing-content/

title: "A Survey of Recent Advances in Edge-Computing-Powered Artificial Intelligence of Things"
subtitle: "【文献精读】基于边缘计算的人工智能研究进展综述"
summary: ""
authors: []
tags: [文献精读, 综述, 边缘智能]
categories: [Academic]
date: 2022-06-06T11:22:43+08:00
lastmod: 2022-06-06T11:22:43+08:00
featured: false
draft: false

## Featured image
## To use, add an image named `featured.jpg/png` to your page's folder.
## Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: true

## Projects (optional).
##   Associate this post with one or more of your projects.
##   Simply enter your project's folder or file name without extension.
##   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
##   Otherwise, set `projects = []`.
projects: []
---

本文是一篇关于边缘计算赋能人工智能物联网 AIoT 的研究综述，于 2021 年发表在 CCF A 类期刊 Internet Things of Journal (IoT-J) 上。

[原文链接](https://ieeexplore.ieee.org/document/9453402)

## Abstract

The Internet of Things (IoT) has created a ubiquitously connected world powered by a multitude of wired and wireless sensors generating a variety of heterogeneous data over time in a myriad of fields and applications. To extract complete information from these data, advanced artificial intelligence (AI) technology, especially deep learning (DL), has proved successful in facilitating data analytics, future prediction and decision making. The collective integration of AI and the IoT has greatly promoted the rapid development of AI-of-Things (AIoT) systems that analyze and respond to external stimuli more intelligently without involvement by humans. However, it is challenging or infeasible to process massive amounts of data in the cloud due to the destructive impact of the volume, velocity, and veracity of data and fatal transmission latency on networking infrastructures. These critical challenges can be adequately addressed by introducing edge computing. This article conducts an extensive survey of an end-edge-cloud orchestrated architecture for flexible AIoT systems. Specifically, it begins with articulating fundamental concepts including the IoT, AI and edge computing. Guided by these concepts, it explores the general AIoT architecture, presents a practical AIoT example to illustrate how AI can be applied in real-world applications and summarizes promising AIoT applications. Then, the emerging technologies for AI models regarding inference and training at the edge of the network are reviewed. Finally, the open challenges and future directions in this promising area are outlined.

作者在摘要当中首先分析了背景 AIoT，并且认为在云中处理海量的数据不可行。而引入边缘计算 Edge Computing，可以充分解决这些关键挑战。作者在本文中对端边云协同架构进行了广泛的调查。具体而言，本文首先阐述了物联网 IoT、人工智能 AI 和边缘计算 Edge Computing 等基本概念。在这些概念的基础上，本文讨论了一般的 AIoT 体系结构，给出了一个实际的 AIoT 示例，以说明如何将人工智能应用于实际应用，并总结了有前途的 AIoT 应用。然后，本文回顾了人工智能模型在网络边缘的推理和训练方面的新兴技术。最后，本文概述了这一前景广阔领域的开放挑战和未来方向。

## Introduction

首先是论文的 Introduction 部分。在这里我将作者的 Introduction 全文翻译，并且梳理其行文逻辑，供参考学习。另外，可以积累一些常用的英语表达。

Benefiting from the extensive use of the Internet and the rapid development of many wired and wireless connected devices, the Internet of Things (IoT) matures promptly and plays an increasingly significant role in every aspect of life by providing many crucial services, such as information exchange and monitoring.

得益于互联网的广泛使用和许多有线和无线连接设备的快速发展，物联网 IoT 迅速成熟，并通过提供许多关键服务（如信息交换和监控）在生活的各个方面发挥着越来越重要的作用。

With the extensive applications of IoTs, the total installed IoT-based devices is projected to amount to approximately 41.6 billion, and nearly 79.4 Zettabytes (ZBs) of data may be generated and consumed in 2025.

随着物联网的广泛应用，预计基于物联网的设备总安装量将达到约 416 亿，2025 年可能会产生和消耗近 794 ZB 的数据。

Thus, some nonnegligible challenges that the IoT faces are explosive data generation and reliable data collection between heterogeneous devices in a wide range of applications covering various backgrounds and requests.

因此，物联网面临的一些不容忽视的挑战是，在覆盖各种背景和请求的广泛应用中，异构设备之间的爆炸性数据生成和可靠数据收集。

Cloud computing plays a crucial role in IoT systems, where the vast resources available in the cloud can provide ubiquitous on-demand computing and storage capabilities to support these devices. Additionally, these data may consist of multimedia information, from images, sounds, and videos to structured data (e.g., temperature and humidity). Advanced tools are needed to glean insights from a large volume of raw data.

云计算在物联网系统中扮演着至关重要的角色，在物联网系统中，云中可用的巨大资源可以提供无处不在的按需计算和存储能力来支持这些设备。此外，这些数据可能包括多媒体信息，从图像、声音和视频到结构化数据（例如温度和湿度）。需要高级工具来从大量原始数据中收集见解。

Facilitated by the recent achievements of algorithms, computing capabilities and big data processing necessities, artificial intelligence (AI), especially its essential sector of deep learning (DL), has achieved unprecedented success in data analysis, future prediction and decision making.

在算法、计算能力和大数据处理需求的最新成就的推动下，人工智能 AI，尤其是其重要的深度学习 DL 部门，在数据分析、未来预测和决策方面取得了前所未有的成功。

Clearly, the AI of Things (AIoT), an integrative technology combining both AI and the IoT, is starting to garner its share of the spotlight with the support of cloud centers. In the AIoT era, large amounts of data generated by IoT devices provide perfect opportunities for training AI models to reliably mine valuable data from a noisy and complex environment for intelligent analysis and decision making.

显然，人工智能物联网 AIoT，一种结合了人工智能和物联网的综合技术，正开始在云中心的支持下获得其聚光灯的份额。在 AIoT 时代，物联网设备生成的大量数据为训练人工智能模型提供了完美的机会，以可靠地从嘈杂复杂的环境中挖掘有价值的数据，进行智能分析和决策。

{{< callout type="info" >}}

作者在这一段当中由物联网 IoT 中的海量数据引出云计算 Cloud Computing 和人工智能 AI 两大概念，并且引出人工智能物联网 AIoT 的概念。

{{< /callout >}}

The cloud-centric AIoT requires the massive amount of heterogeneous data collected from IoT sensors to be transmitted to the cloud center through a wide-area network (WAN) for further processing and analysis before delivering the feedback to end devices.

以云为中心的 AIoT 要求从物联网传感器收集的大量异构数据通过广域网（WAN）传输到云中心，以便在向终端设备提供反馈之前进行进一步处理和分析。

Although the cloud center has unlimited computational capacity, such a cloud-based AIoT architecture is ill-suited for time-critical and privacy-sensitive applications due to the great pressure on network bandwidth, the inherent latency constraints of network communication and the potential to expose private and sensitive information during data offloading and remote processing.

尽管云中心具有无限的计算能力，但这种基于云的 AIoT 体系结构不适合时间关键型和隐私敏感型应用程序，因为网络带宽压力巨大，网络通信固有的延迟限制，以及在数据卸载和远程处理过程中暴露私有和敏感信息的可能性。

Edge computing seems to be a promising technique to remedy these issues, which brings computational resources closer to the data source with a relatively light access burden and a low transmission delay.

边缘计算似乎是解决这些问题的一种很有前途的技术，它以相对较轻的访问负担和较低的传输延迟使计算资源更接近数据源。

It is extremely suitable for the AIoT because AI models, especially DL models, that depend greatly on computation and storage resources can still work fluently and cooperatively by partitioning the layers into several parts and offloading the computation-intensive tasks to edge servers.

它非常适合 AIoT，因为人工智能模型，尤其是深度学习模型，在很大程度上依赖于计算和存储资源，通过将层划分为几个部分并将计算密集型任务卸载到边缘服务器，仍然可以流畅地协同工作。

Such a computing paradigm coupled with AI can assist users better and more intelligently, where AI models function as a powerful tool to mine valuable information from raw data, make real-time decisions and to dynamically manage various resources of the edge platforms.

这种与人工智能相结合的计算范式可以更好、更智能地帮助用户，其中人工智能模型可以作为一种强大的工具，从原始数据中挖掘有价值的信息，做出实时决策，并动态管理边缘平台的各种资源。

Rather than transmit all the raw data to the cloud for overall analysis, edge computing-assisted AIoT solutions essentially enable AI models to work in the field.

边缘计算辅助的 AIoT 解决方案本质上使人工智能模型能够在本地工作，而不是将所有原始数据传输到云进行全面分析。

These solutions can lighten the burden of data transmission through the network backhaul, further reduce the cost of network processing and maintenance and make timely decisions by positioning computational capabilities near end devices. Additionally, these methods protect sensitive data from being abused by illegal operators or hijacked by attackers.

这些解决方案可以减轻通过网络回程传输数据的负担，进一步降低网络处理和维护的成本，并通过在终端设备附近定位计算能力及时做出决策。此外，这些方法可以保护敏感数据不被非法操作员滥用或被攻击者劫持。

{{< callout type="info" >}}

作者在这一段由基于云中心的 AIoT 存在的带宽限制和隐私安全问题，引出了边缘计算辅助的 AIoT 解决方案，并且分析边缘计算范式更好的原因。

{{< /callout >}}

This article investigates convergence of AI and the IoT from the perspective of end-edge-cloud collaboration, where immediate and real-time responses are enabled by using AI capacities for processing raw data at end or edge devices and higher accuracy results are gained by using cloud analytics in collaboration.

本文从端边云协同的角度研究了人工智能与物联网的融合，其中通过使用人工智能处理终端或边缘设备原始数据的能力实现即时和实时响应，并通过协作使用云分析获得更高精度的结果。

The AIoT can bring numerous benefits to human beings in a spectrum of domains and form a ubiquitous intelligent collaborative environment; however, significant challenges must be overcome before fully realizing the potential of AIoT. Thus, this article aims to present a comprehensive survey of recent advances, open challenges and future directions for the AIoT.

AIoT 可以在多个领域为人类带来诸多利益，形成无处不在的智能协作环境；然而，在充分发挥 AIoT 的潜力之前，必须克服重大挑战。因此，本文旨在全面综述 AIoT 的最新进展、开放挑战和未来方向。

至此，作者已经给出了本文的简要逻辑。在 Introduction 的剩余部分中，作者分三节总结了相关工作、本文的贡献以及本文的行文结构。

### Related Work

Several published references present AI and machine learning (ML) or DL methods that have been used in the domain of the IoT.

作者在相关工作一节主要介绍了一些已发表的综述，它们都介绍了物联网领域的人工智能和机器学习或深度学习方法。相关内容见下表：

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-mya0{border-color:#000000;font-size:18px;text-align:center;vertical-align:top}
.tg .tg-m916{border-color:#000000;font-size:18px;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-mya0">Title</th>
    <th class="tg-mya0">Year</th>
    <th class="tg-mya0">Topic</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-mya0"><a href="https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/trit.2018.1008" target="_blank" rel="noopener noreferrer">Artificial intelligence in Internet of Things</a></td>
    <td class="tg-m916">2018</td>
    <td class="tg-mya0">AIoT</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://www.sciencedirect.com/science/article/pii/S0167739X19304030" target="_blank" rel="noopener noreferrer">Machine learning in the Internet of Things: Designed techniques for smart cities</a></td>
    <td class="tg-m916">2019</td>
    <td class="tg-mya0">ML; IoT</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://ieeexplore.ieee.org/document/9052677" target="_blank" rel="noopener noreferrer">Edge intelligence: The confluence of edge computing and artificial intelligence</a></td>
    <td class="tg-m916">2020</td>
    <td class="tg-mya0">Edge Intelligence</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://link.springer.com/article/10.1007/s13042-018-0834-5" target="_blank" rel="noopener noreferrer">A survey on application of machine learning for Internet of Things</a></td>
    <td class="tg-m916">2018</td>
    <td class="tg-mya0">ML; IoT</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://ieeexplore.ieee.org/document/8373692" target="_blank" rel="noopener noreferrer">Deep learning for IoT big data and streaming analytics: A survey</a></td>
    <td class="tg-m916">2018</td>
    <td class="tg-mya0">IoT; DL</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://dl.acm.org/doi/10.1145/3398209" target="_blank" rel="noopener noreferrer">Deep Learning on Mobile and Embedded Devices: State-of-the-art, Challenges, and Future Directions</a></td>
    <td class="tg-m916">2021</td>
    <td class="tg-mya0">DL; Mobile and Embedded Devices</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://ieeexplore.ieee.org/document/8270639" target="_blank" rel="noopener noreferrer">Learning IoT in Edge: Deep Learning for the Internet of Things with Edge Computing</a></td>
    <td class="tg-m916">2018</td>
    <td class="tg-mya0">IoT; Edge Computing</td>
  </tr>
  <tr>
    <td class="tg-mya0"><a href="https://ieeexplore.ieee.org/document/8763885" target="_blank" rel="noopener noreferrer">Deep Learning With Edge Computing: A Review</a></td>
    <td class="tg-m916">2019</td>
    <td class="tg-mya0">DL; Edge Computing</td>
  </tr>
</tbody>
</table>

### Contributions of This Survey

1. An overview of fundamental technologies supporting the AIoT are given in terms of the general architecture of the IoT, state-of-the-art AI methods accompanied by key characteristics, and edge computing-related paradigms along with corresponding hardware and systems.

根据物联网的一般架构、最先进的人工智能方法以及关键特征、边缘计算相关范式以及相应的硬件和系统，概述了支持人工智能应用的基本技术。

2. Confluence of AI and the IoT is the core of this article. In this respect, benefits of incorporating AI into IoT systems are first illustrated. An end-edge-cloud collaborative architecture of AIoT are then proposed. A practical example of AIoT applications is additionally given to further illustrate how AI can be applied in real-world applications.

人工智能与物联网的融合是本文的核心。在这方面，首先说明了将人工智能纳入物联网系统的好处。在此基础上，提出了一种 AIoT 的端边云协同体系结构。此外，还提供了一个 AIoT 应用的实际示例，以进一步说明人工智能如何应用于实际应用中。

3. Some promising applications of AIoT are surveyed in a variety of domains, such as the IoV, smart healthcare, smart industry, smart homes, smart agriculture, smart grids and smart environment.

AIoT 在许多领域都有着很好的应用前景，如 IoV、智能医疗、智能工业、智能家居、智能农业、智能电网和智能环境。

4. The recent approaches and technologies for performing AI inference on an AIoT hierarchy from resource-hungry end devices to edge servers and the cloud are summarized.

总结了在 AIoT 层次结构上执行人工智能推理的最新方法和技术，从资源匮乏的终端设备到边缘服务器和云。

5. The enabling technologies for decentralized AI training among various end devices and edge servers of an AIoT hierarchy are discussed.

讨论了在 AIoT 层次结构的各种终端设备和边缘服务器之间进行分散式人工智能训练的使能技术。

6. The open challenges and future directions for constructively and fruitfully merging of AI and the IoT are outlined.

概述了人工智能和物联网建设性和富有成效地融合的开放挑战和未来方向。

### Outline of This Survey

{{< figure src="architecture.svg" >}}

## Fundamentals of Artificial Intelligence of Things

This section reviews the general architecture of the IoT in brief, then presents basic AI models with an emphasis on ML and DL models and additionally gives an overview of edge computing in terms of related paradigms, relationship with the fifth generation (5G), hardware, and systems.

作者在本节简要回顾了物联网的总体架构，然后介绍了基本的人工智能模型，重点介绍了ML和深度学习模型，并从相关范式、与 5G 的关系、硬件和系统等方面概述了边缘计算。

### Introduction to the Internet of Things

Generally, the IoT architecture is composed of three layers, namely, the perception layer, network layer and application layer.

作者认为，物联网架构一般由感知层、网络层和应用层三层组成。

{{< figure src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6488907/9530274/9453402/liu1-3088875-large.gif" >}}

1. **Perception Layer**: The perception layer provides the core capability enabling the comprehensive awareness of the environment; this layer includes such diverse devices and technologies as sensors, actuators, radio-frequency identification (RFID), 2-D codes, and multimedia information collection devices. These devices are used mainly to sense and collect physical data, and data is generally produced in trillions of bytes with a variety of attributes, including various physical quantities, identity signs, location information, and audio and video data. Additionally, these devices can respond to the environment.

感知层提供了能够全面感知环境的核心能力；该层包括传感器、执行器、射频识别（RFID）、二维码和多媒体信息采集设备等多种设备和技术。这些设备主要用于感知和收集物理数据，数据通常以万亿字节的形式生成，具有各种属性，包括各种物理量、身份标志、位置信息以及音频和视频数据。此外，这些设备可以响应环境。

2. **Network Layer**: The network layer is the most standardized among the three layers of the IoT, in which the devices in the perception layer can communicate with IoT gateways, wireless-fidelity (Wi-Fi) access points (APs) and base stations (BSs) to transmit data to other parts quickly, accurately and safely. This layer enables a device to communicate at a short-range to long-range distance by using a variety of communication protocols, such as wired and wireless networks, including Bluetooth, ZigBee, Sigfox, long-range radio (LoRa), and Narrowband IoT (NB-IoT). The data generated in the perception layer need to be transmitted to the server via the network layer promptly and accurately.

网络层是物联网三层中最标准化的一层，其中感知层的设备可以与物联网网关、无线局域网（Wi-Fi）接入点（AP）和基站（BSs）进行通信，以快速、准确、安全地向其他部分传输数据。该层通过使用各种通信协议，例如有线和无线网络，包括蓝牙、ZigBee、Sigfox、远程无线电（LoRa）和窄带物联网（NB-IoT），使设备能够在短距离到长距离之间进行通信。感知层生成的数据需要通过网络层及时准确地传输到服务器。

3. **Application Layer**: The application layer is equivalent to the control layer and decision-making layer of the IoT, in which a mass of polymorphic and heterogeneous data with rich semantics are analyzed. The application layer can provide a myriad of applications, such as industrial control, urban management, power monitoring, and green agriculture.

应用层相当于物联网的控制层和决策层，分析了大量语义丰富的多态异构数据。应用层可以提供多种应用，如工业控制、城市管理、电力监控和绿色农业。

### Basics of Artificial Intelligence

Algorithms exert a crucial function in AI, where simple algorithms can be applicable to simple applications, while more complex ones can build strong AI.

算法在人工智能中发挥着至关重要的作用，简单的算法可以应用于简单的应用程序，而更复杂的算法可以构建强大的人工智能。

Typically, ML, a subset of AI, is the most mainstream method used by systems to automatically learn from the data, identify patterns and make decisions from experience without human intervention or assistance.

通常，机器学习 ML 是人工智能的一个子集，是系统在无需人工干预或帮助的情况下自动从数据中学习、识别模式和根据经验做出决策的最主流方法。

DL, a unique branch of ML, is quite different from classic ML algorithms, which uses a hierarchical neural network to make the model more complex and enables automatic learning by absorbing a great deal of unstructured data, such as images, sound, text and video.

深度学习 DL 是 ML 的一个独特分支，与经典ML算法有很大不同，后者使用层次神经网络使模型更加复杂，并通过吸收大量非结构化数据（如图像、声音、文本和视频）实现自动学习。

This section will introduce several traditional ML algorithms and present some typical neural network algorithms accompanied with the corresponding functions, including a distinctive reinforcement learning (RL) method.

作者在本节将介绍几种传统的 ML 算法，并介绍一些典型的神经网络算法以及相应的函数，包括一种独特的强化学习 RL 方法。

下面的内容是对作者接下来介绍 ML 算法的简要概括。

#### Traditional Machine Learning: 传统机器学习

- Support vector machine (SVM): 支持向量机
- Decision tree (DT): 决策树
- k-means clustering: k-均值聚类

#### Neural Networks: 神经网络

- Multilayer perceptron (MLP): 多层感知机
- Convolutional neural network (CNN): 卷积神经网络
- Recurrent neural network (RNN): 循环神经网络
- Long short-term memory (LSTM): 长短期记忆网络
- Generative adversarial network (GAN): 生成对抗网络

#### Reinforcement Learning: 强化学习

- Value-based deep Q-learning: 基于价值的深度 Q-学习
- Policy-based deep Q-learning: 基于策略的深度 Q-学习

可以看到，作者是按照人工智能的发展来进行介绍的，即从机器学习，到深度学习，再到强化学习。

### Overview of Edge Computing

Cloud computing refers to the concept of delivering different services on demand by using networking, virtualization, distributed computing, utility computing and software services. Cloud computing is a service-oriented architecture that provides flexible services, reduces the information technology overhead for end users, and the total cost of ownership.

云计算是指通过使用网络、虚拟化、分布式计算、效用计算和软件服务按需提供不同服务的概念。云计算是一种面向服务的架构，它提供灵活的服务，减少最终用户的信息技术开销，并降低总体拥有成本。

However, the cloud center is usually built in a remote area far from end users, thus possibly causing data transmission delays. With a soaring number of IoT devices, the cloud cannot satisfy the requirements of latency-sensitive and privacy-critical applications.

然而，云中心通常建在远离最终用户的偏远地区，因此可能导致数据传输延迟。随着物联网设备数量的激增，云无法满足延迟敏感和隐私关键应用程序的要求。

The emergence of edge computing is aimed at migrating computational tasks to edge devices near sensors and actuators, which can alleviate the pressure of data transmission, reduce end-to-end latency, and thus enable real-time services.

边缘计算的出现旨在将计算任务迁移到传感器和执行器附近的边缘设备，这可以缓解数据传输的压力，减少端到端延迟，从而实现实时服务。

A diversity of devices can serve as edge computing platforms: switches, cellular BSs or IoT gateways, which makes edge computing flexible and scalable deploy various services at anywhere between end users and the cloud. Typically, edge computing is considered an extension of the cloud platform and works independently and effectively in some scenarios or collaborates with the cloud platform.

多种设备可以用作边缘计算平台：交换机、蜂窝基站或物联网网关，这使得边缘计算灵活且可扩展，可以在最终用户和云之间的任何位置部署各种服务。通常，边缘计算被视为云平台的扩展，在某些场景中独立有效地工作，或与云平台协作。

This section reviews edge computing-related paradigms, the relationship between 5G and edge computing, and edge computing hardware and systems.

本节回顾边缘计算相关范例、5G 与边缘计算之间的关系以及边缘计算硬件和系统。

#### Edge Computing-Related Paradigms: 边缘计算相关范式

- Cloudlet: 由卡内基梅隆大学提出的 Cloudlet 被设想为一个移动增强型数据中心，具有一定的计算和存储能力，位于移动设备附近。Cloudlet 被认为是移动设备、微云和云三层架构的中间层。
- Fog computing: 最初由思科提出的雾计算被认为是对传统云计算的有效扩展和补充，它将资源和服务（计算、存储、网络和处理）放置在从终端设备到云的路径上。
- Mobile-edge computing: 移动边缘计算由欧洲电信标准协会 ETSI 标准化，通过在蜂窝网络边缘（如无线基站）分配计算和存储资源来提供服务。

#### Fifth-Generation Mobile Networks and Edge Computing: 5G 移动网络与边缘计算

5G technology standard is seen as the most promising wireless cellular network standard to cater to the requirements of next-generation networks. Many ultradense edge devices will be deployed in 5G systems, including mainly small cell BSs and wireless APs. These devices are often equipped with certain computing and storage abilities, thus enabling ubiquitous mobile computing.

5G 技术标准被视为最有希望满足下一代网络需求的无线蜂窝网络标准。许多超密集边缘设备将部署在 5G 系统中，主要包括小蜂窝基站和无线接入点。这些设备通常具有一定的计算和存储能力，从而实现无处不在的移动计算。

#### Edge Computing Hardware: 边缘计算硬件

- Application-Specific Integrated Circuit (ASICs) Chip: 专用集成电路芯片
- Graphics Processing Unit-Based (GPU-Based) Product: 基于图形处理单元的产品
- Field-Programmable Gate Array (FPGA)-Based Device: 基于现场可编程门阵列的设备
- Brain-Inspired Chip: 脑启发芯片

#### Edge Computing Systems: 边缘计算系统

- [Azure IoT Edge](https://azure.microsoft.com/zh-cn/services/iot-edge/)
- [EdgeX Foundry](https://cn.edgexfoundry.org/)
- [Apache Edgent](https://incubator.apache.org/projects/edgent.html)
- [Central Office Rearchitected as a Datacenter (CORD)](https://opennetworking.org/cord/)
- [Akraino Edge Stack](https://wiki.akraino.org/display/AK/Akraino+Edge+Stack)

## Artificial Intelligence of Things

In this section, opportunities to fuse AI and the IoT, the general AIoT architecture with the support of edge computing and the cloud, and a practical example of AIoT applications will be reviewed.

在本节中，作者回顾了人工智能和物联网融合的因素、支持边缘计算和云的一般 AIoT 架构，以及 AIoT 应用的一个实际示例。

### Opportunities for Integrating Artificial Intelligence With the Internet of Things

The data generated by IoT devices have many properties, namely, polymorphism, heterogeneity, timeliness, accuracy, massive-scale and rich semantics. Real-time data for all events must be processed promptly. AI can effectively and efficiently mine valuable information from these data and make decisions. Moreover, AI models can be deployed on every layer of IoT systems with enhanced performance. The synergy of AI and IoT is named AIoT, benefits of which are illustrated as follows.

作者认为，人工智能与物联网深度融合的机遇源于：

- 物联网设备生成的数据具有多态性、异构性、及时性、准确性、大规模和丰富的语义等特性。
- 物联网设备处理数据必须确保实时性。
- 人工智能可以有效地从这些数据中挖掘有价值的信息并作出决策。
- 人工智能可以部署在物联网系统的每一层上。

作者认为，AIoT 的优势在于：

- High Flexibility: 高度的灵活性
- Enhanced Interactivity: 增强的交互性
- Intelligent Decisions and Accurate Predictions: 智能的决策和精准的预测
- Various Applications: 各种应用程序

### General Architecture of Artificial Intelligence of Things

From bottom to top are the end layer, edge layer and cloud layer, and the cloud layer can coordinate the end layer and the edge layer. The end layer can proprocess or analyze data on premises and make early decisions. The proprocessed data from the end layer can be aggregated in the edge or cloud layer for deep disposal.

作者认为，AIoT 架构具有和 IoT 类似的端边云三层架构。从下到上依次为端层、边缘层和云层，云层可以协调端层和边缘层。终端层可以在本地预处理或分析数据，并做出早期决策。来自端层的预处理数据可以聚集在边缘层或云层中进行深度处理。

{{< figure src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6488907/9530274/9453402/liu4-3088875-large.gif" >}}

### Example of Artificial Intelligence of Things Applications

The following describes the corresponding system design, illustrates model training and deployment as well as inference and provides a case study using an end-to-end AI model.

作者在本章介绍一个 AIoT 的应用 HydraMini，一个自动驾驶汽车系统，并以此为例，说明了模型训练和部署以及推理的过程，并提供了使用端到端人工智能模型的案例研究。

{{< figure src="https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/6488907/9530274/9453402/liu5-3088875-small.gif" >}}

由于篇幅有限，本文在这里不对该系统进行详细的描述，仅以上图供参考。

## Applications of Artificial Intelligence of Things

In this section, several application scenarios, including smart homes, smart healthcare, smart agriculture, smart industry, smart agriculture, smart grids and smart environment, are presented to demonstrate how edge computing aided AIoT systems will make real-world more efficient, smarter and safer.

作者在本章介绍了几个应用场景，包括智能家居、智能医疗、智能农业、智能工业、智能农业、智能电网和智能环境，以演示边缘计算辅助的 AIoT 系统如何使现实世界更加高效、智能和安全。

### Internet of Vehicles

The IoV enabled by AIoT aims to enhance road safety, strengthen efficiency, decrease crash risks and lower traffic congestion in transportation systems. Currently, the IoV covers three major categories: 1) AD; 2) monitoring systems for safe driving; and 3) cooperative vehicle infrastructure systems (CVISs).

作者总结认为，AIoT 启用的 IoV 旨在提高道路安全、提高效率、降低碰撞风险和降低交通系统中的交通拥堵。目前，IoV 涵盖三大类：

1. Autonomous Driving: 自动驾驶
2. Monitoring Systems for Safe Driving: 安全驾驶监控系统
3. Cooperative Vehicle Infrastructure Systems (CVISs): 合作车辆基础设施系统

### Smart Healthcare

The era of edge-computing-enabled AIoT opens a new line of research in the field of medical and healthcare systems, which has already provided a myriad of applications, including health monitoring systems, disease diagnosis systems, and auxiliary therapy systems.

边缘计算时代开启了医疗和保健系统领域的新研究领域，该领域已经提供了无数应用，包括：

1. Health Monitoring Systems: 健康监测系统
2. Disease Diagnosis Systems: 疾病诊断系统
3. Auxiliary Therapy Systems: 辅助治疗系统

### Smart Industry

The fourth industrial revolution, also known as Industry 4.0, has created new opportunities for product robotization and automation, which emphasize intelligent manufacturing techniques. The edge-computing-aided AIoT caters to the requirements of smart manufacturing, where edge computing enables low-latency, secure manufacturing while AI provides more intelligent local analysis and prediction. Smart industry focuses mainly on production automation and smart data analysis.

第四次工业革命，也称为工业 4.0，为强调智能制造技术的产品机器人化和自动化创造了新的机遇。边缘计算辅助的 AIoT 迎合了智能制造的需求，边缘计算实现了低延迟、安全的制造，而人工智能提供了更智能的局部分析和预测。智能产业主要专注于生产自动化和智能数据分析。

作者总结了如下具体应用场景：

1. Smart Manufacturing: 智能制造
2. Smart Industry Analysis: 智能行业分析

### Smart Homes

The rapid development of AIoT has encouraged many attractive computationally intensive applications that provide intelligent sensing and convenient control services in smart home scenarios. For home data protection, edge computing has emerged as an excellent option to execute local computation and processing, especially for some computation-intensive AI-based applications.

AIoT 的快速发展鼓励了许多有吸引力的计算密集型应用，这些应用在智能家居场景中提供智能传感和方便的控制服务。对于家庭数据保护，边缘计算已经成为执行本地计算和处理的一个很好的选择，特别是对于一些计算密集型 AI 应用程序。

### Smart Agriculture

Smart agriculture aims to improve crop yield and quality, reduce labor costs and protect the environment from the excessive use of pesticides and fertilizers by using modern technologies. The explosive employment of sensors and automated equipment will generate an abundance of data, thereby taxing the Internet and cloud center. Edge-computing-aided AIoT applications enable data to be processed locally or on nearby edge servers to seek a timely response. Generally, smart agriculture concentrates on crop production, agriculture environment monitoring and agriculture security.

智能农业旨在利用现代技术提高作物产量和质量，降低劳动力成本，保护环境免受农药和肥料过度使用的影响。传感器和自动化设备的爆炸性使用将产生大量数据，从而给互联网和云中心带来负担。边缘计算辅助的 AIoT 应用程序可以在本地或附近的边缘服务器上处理数据，以寻求及时的响应。一般来说，智能农业集中于作物生产、农业环境监测和农业安全。

作者例举了一些具体的在农业方面的应用：

1. Crop Production Analysis: 作物产量分析
2. Agriculture Environment Monitoring: 农业环境监测
3. Agriculture Security: 农业安全

### Smart Grids

Grid operators have deployed IoT sensors to monitor power grid devices in real time. Recently, there has been a rush to integrate AI with electrical grids to provide a more stable, cost-saving and secure smart grid.

电网运营商已部署物联网传感器来实时监控电网设备。最近，人们纷纷将人工智能与电网集成，以提供更稳定、更节省成本和更安全的智能电网。

作者在这里例举了很多文献介绍 AIoT 在智能电网重点应用，这里不再赘述。

### Smart Environment

The goal of smart environment is to provide humans with a safer and more comfortable life. Environmental monitoring systems can send early warnings to humans by making accurate predictions.

作者认为，AIoT 也可以应用于环境监测，这里同样也不再赘述。

## Enabling Technologies for Artificial Intelligence Inference in Artificial Intelligence of Things

Most AI models, especially DNN models, are designed to be much deeper, which have a larger data set to promote their accuracy. Inference in the cloud will inadvertently incur additional queuing and propagation delays from the network, which is fatal for time-critical applications. These AI models, however, are too large and computationally expensive to be directly deployed on resource-constrained end devices.

大多数人工智能模型，尤其是 DNN 模型，设计得更深入，有更大的数据集来提高其准确性。云中的推理将无意中导致额外的排队和网络传播延迟，这对于时间关键型应用程序来说是致命的。然而，这些人工智能模型太大，计算成本太高，无法直接部署在资源受限的终端设备上。

To overcome this challenge, one possible approach is to simplify the models with a dramatic decrease in computation. The other effective approach is to outsource complex inference tasks to edge nodes with more resources. In this regard, the methods used to optimize inference on device and coinference in the edge, and privacy-preserving techniques, are surveyed.

为了克服这一挑战，一种可能的方法是简化模型，大大减少计算量。另一种有效的方法是将复杂的推理任务外包给具有更多资源的边缘节点。在这方面，综述了用于优化设备上的推理和边缘中的共指的方法，以及隐私保护技术。

基于上述思路，作者将 AIoT 模型推理分为三种模式：端上推理、边缘协同推理和私密推理。

### On-Device Inference

Generally, two practical methods can be used to reduce computational costs of AI models. One is to directly design compact and efficient neural network models with a reduced number of parameters, such as SqueezeNet, Xception, and ShuffleNet. The other method is typically called model compression, which achieves a smaller memory footprint and improved operation for end devices by compressing pretrained networks.

通常，可以使用两种实用方法来降低人工智能模型的计算成本。一种是直接设计紧凑、高效的神经网络模型，减少参数数量。另一种方法通常称为模型压缩，它通过压缩预训练网络来实现较小的内存占用和改进终端设备的操作。

#### Designing Compact Networks: 设计紧凑高效的网络

- [SqueezeNet](https://arxiv.org/abs/1602.07360)
- [Xception](https://ieeexplore.ieee.org/document/8099678)
- [ShuffleNet](https://ieeexplore.ieee.org/document/8578814)
- [MobileNet](https://linkinghub.elsevier.com/retrieve/pii/S1383762118304612)

#### Model Compression: 模型压缩

##### Parameter pruning and sharing: 参数剪枝与共享

Parameter pruning and sharing can decrease the number of redundant parameters and address the issue of overfitting. Model pruning methods are roughly divided into structural pruning and nonstructural pruning.

参数剪枝和共享可以减少冗余参数的数量，并解决过拟合问题。模型剪枝方法大致分为结构性剪枝和非结构性剪枝。

Nonstructural pruning is generally a connection-level, fine-grained pruning method with relatively high accuracy; however, it depends on a specific algorithm library or hardware platform, such as deep compression or sparse-winograd. 

非结构性剪枝通常是一种连接级别的细粒度剪枝方法，具有较高的精度；然而，它取决于特定的算法库或硬件平台，例如 [deep compression](https://arxiv.org/abs/1510.00149) 或 [sparse-winograd](https://arxiv.org/abs/1802.06367)。

Structural pruning is a filter-level or layer-level coarse-grained pruning method with relatively low accuracy, and the structural pruning strategy is more effective than nonstructural pruning and does not depend on a specific algorithm library or hardware platform.

结构剪枝是一种精度相对较低的过滤器级或层级粗粒度剪枝方法，结构剪枝策略比非结构剪枝更有效，不依赖于特定的算法库或硬件平台。

##### Quantization: 量化

Quantization uses a more compact format by adopting low-bit width numbers instead of 32-bit floating-point numbers to represent each weight, thereby reducing the computational intensity and the memory footprint and further increasing the energy efficiency.

量化使用更紧凑的格式，通过采用低位宽度数字而不是 32 位浮点数字来表示每个权重，从而降低计算强度和内存占用，并进一步提高能效。

##### Knowledge distillation: 知识蒸馏

Knowledge distillation fabricates a compact DNN model that migrates the behavior from a powerful and complex DNN model. By training the smaller DNN model by using the output predictions generated by the complicated model, the smaller DNN model should approach or exceed the function trained by the larger DNNs as well as possible.

知识蒸馏构建了一个紧凑的 DNN 模型，该模型将行为从强大而复杂的 DNN 模型迁移过来。通过使用复杂模型生成的输出预测对较小的 DNN 模型进行训练，较小的 DNN 模型应尽可能接近或超过较大 DNN 训练的函数。

### Coinference at the Edge

Deploying large-size AI models, which require high computation, power and memory capacity from the end infrastructures, remains a challenge. Therefore, it is a good option to segment DNN models into multiple partitions and offload each part to heterogeneous local end devices, more powerful distributed edge servers or remote cloud servers.

部署大型人工智能模型仍然是一个挑战，因为它需要终端基础设施提供高计算、高功耗和高内存容量。因此，将 DNN 模型划分为多个分区并将每个部分卸载到异构本地终端设备、更强大的分布式边缘服务器或远程云服务器是一个很好的选择。

作者于是总结了实现这种协同推理的技术如下：

#### Offloading: 卸载

Computation offloading is a widely used distributed computing paradigm in fast inference, where an end device can migrate part of its computation to an edge node, the cloud, or both over a heterogeneous network. By this means, offloading can employ remote servers to increase the computation speed and save energy. However, a compromise between advantages in remote execution and sacrifices in data transmission should be reached.

计算卸载是快速推理中广泛使用的分布式计算范式，终端设备可以通过异构网络将部分计算迁移到边缘节点、云或两者。通过这种方式，卸载可以使用远程服务器来提高计算速度并节省能源。不过，应该在远程执行的优势和数据传输的牺牲之间达成妥协。

#### DNN Model Partitioning: 模型切分

The idea of offloading can be extended to model partitioning, which takes advantage of the unique structure of DNNs. In this way, the layers of DNNs can be divided into several parts, where some layers are directly executed on end device and some layers are offloaded to edge server or the cloud for remote computation.

卸载的思想可以扩展到模型切分，它利用了 DNN 的独特结构。这样，DNN 的层可以分为几个部分，其中一些层直接在终端设备上执行，一些层卸载到边缘服务器或云上进行远程计算。

#### Model Early Exit 模型提前退出

A DNN model with additional layers can generally achieve higher accuracy; however, the model requires increased computation and energy resources in feed-forward inference. Therefore, it is difficult to execute such a complicated DNN model on a resource-constrained end device.

具有附加层的 DNN 模型通常可以实现更高的精度；然而，该模型需要增加前馈推理的计算量和能量资源。因此，很难在资源受限的终端设备上执行如此复杂的 DNN 模型。

The idea of accelerating model inference can be further promoted by the emerging model early exit method, which leverages additional side branch layers to obtain the classification result. The inference process can be completed in advance via the early classifiers with high confidence. It is also possible for some complicated tasks to use more DNN layers to complete the classification procedure.

新兴的模型提前退出方法可以进一步促进加速模型推理的思想，该方法利用额外的边分支层来获得分类结果。通过提前的分类器可以提前完成推理过程，并且具有很高的可信度。对于一些复杂的任务，也可以使用更多的 DNN 层来完成分类过程。

### Private Inference

… However, this kind of cooperative inference system also faces privacy concerns when the data including sensitive information is transmitted to a nearby edge server or cloud. Additionally, end devices are too energy and resource constrained to execute complex data protection methods. Intuitively, it is worth studying privacy enhancement between end devices and edge servers.

当包含敏感信息的数据传输到附近的边缘服务器或云时，这种协同推理系统也面临隐私问题。此外，终端设备的能源和资源过于有限，无法执行复杂的数据保护方法。直观地说，值得研究终端设备和边缘服务器之间的隐私增强。

In this section, secure computation through encryption or cryptography and data obfuscation techniques are proposed for the AIoT inference.

作者在本节中，提出了 AIoT 推理的概念。具体而言，包括如下技术：

#### Secure Computation: 安全计算

Cryptography-based methods can be applied to AIoT privacy inference. Edge servers perform computation by using the data preserved by cryptographic techniques while knowing nothing about the data, and end devices receive the result of inference without knowing the model.

基于密码学的方法可以应用于 AIoT 隐私推断。边缘服务器使用加密技术保存的数据执行计算，而对数据一无所知，终端设备在不知道模型的情况下接收推断结果。

#### Data Obfuscation: 数据混淆

To avoid the heavy computation of cryptographic primitives, data obfuscation can provide a strong guarantee for sensitive data by adaptively injecting noise into data set while retaining the servers’ ability to implement AIoT inference tasks.

为了避免密码原语的繁重计算，数据混淆可以通过自适应地向数据集中注入噪声，同时保持服务器执行 AIoT 推理任务的能力，为敏感数据提供强有力的保障。

## Enabling Technologies for Artificial Intelligence Training in Artificial Intelligence of Things

Conventionally, the training mode of AIoT models relies on a centralized style, which may incur additional costs in data transmission and privacy issues. To effectively address these issues, a decentralized training mode is proposed, where the AI model is divided into several subnetworks
and each part is trained directly on end device with local data. The trained model updates can be aggregated at edge nodes in the network or be exchanged through the interconnect end devices in the network.

传统上，AIoT 模型的训练模式依赖于集中式，这可能会在数据传输和隐私问题上产生额外成本。为了有效解决这些问题，提出了一种分布式的训练模式，将人工智能模型划分为若干子网络，每个部分直接在终端设备上使用本地数据进行训练。经过训练的模型更新可以在网络中的边缘节点聚合，也可以通过网络中的互连终端设备进行交换。

The two kinds of decentralized training modes can be realized without the support of the cloud. In this section, enabling techniques for decentralized AI model training, communication efficiency and security enhancement in AIoT are mainly discussed.

作者认为，这两种分布式的训练模式可以在没有云支持的情况下实现。作者在本节主要讨论了分布式人工智能模型训练的使能技术、AIoT 中的通信效率和安全增强。

### Decentralized Artificial Intelligence of Things Model Training Methods

With respect to the AIoT, it is essential to develop decentralized AI training methods that can avoid data transmission, further reducing the transition bandwidth and enhancing privacy. In this subsection, enabling techniques for decentralized AIoT model training are introduced.

关于AIoT，必须开发分布式的人工智能训练方法，以避免数据传输，进一步减少过渡带宽并增强隐私。作者在本节讨论了分布式 AIoT 模型训练的使能技术。

#### Federated Learning: 联邦学习

FL is a collaborative AI setting that is originally aimed at addressing the problem of Android mobile terminal users updating models locally with unreliable and slow network connections.

联邦学习是一种协作式人工智能设置，最初旨在解决 Android 移动终端用户使用不可靠且缓慢的网络连接在本地更新模型的问题。

Gradually, FL has come to assist in efficient AI training by using data distributed over a large number of end devices and edge servers while ensuring information security, protecting terminal and user privacy, and adhering to legal requirements during data exchange.

通过使用分布在大量终端设备和边缘服务器上的数据，同时确保信息安全，保护终端和用户隐私，并在数据交换过程中遵守法律要求，联邦学习逐渐开始辅助高效的人工智能训练。

Traditionally, in the distributed configuration of FL, the AI model is built without direct access to data, while mobile devices serving as clients carry out local training.

传统的联邦学习的分布式配置中，人工智能模型是在不直接访问数据的情况下构建的，而作为客户端的移动设备则执行本地训练。

Additionally, these mobile devices can be extended to end devices, while edge nodes and cloud servers are equivalently considered as clients. A server coordinates a series of nodes, thereby enabling the clients to take responsibility for various levels of ML model training and share the individual trained models with the server. The server creates a federated model by using the uploaded trained models and returns the optimized model to the clients.

此外，这些移动设备可以扩展到终端设备，而边缘节点和云服务器被等效地视为客户端。服务器协调一系列节点，从而使客户端能够负责不同级别的 ML 模型训练，并与服务器共享各个经过培训的模型。服务器使用上传的经过训练的模型创建一个联邦模型，并将优化后的模型返回给客户端。

#### DNN Splitting: 分裂学习

DNN splitting exchanges partially processed data instead of raw data between end devices and edge servers, which is an effective way to protect privacy-sensitive data.

DNN 拆分在终端设备和边缘服务器之间交换部分处理的数据而不是原始数据，这是保护隐私敏感数据的有效方法。

However, selecting an appropriate splitting point to meet the requirement of latency remains as a research point.

然而，选择合适的分割点来满足延迟的要求仍然是一个研究点。

To reduce the computational complexity with accuracy preserved and introduce a bottleneck, it is proposed in [171] to employ network distillation to distill the head portion of the split model. This approach deploys lightweight models on end side and pushes the intensive computation of DNN to the server, minimizing processing load at the mobile device as well as the amount of wirelessly transferred data.

作者指出，相关工作建议使用蒸馏的方法以在终端部署轻量化模型，并将密集的 DNN 计算推送到服务器，从而最小化移动设备上的处理负载以及无线传输的数据量。

#### Transfer Learning 迁移学习

Knowledge transfer learning, also known as TL, has emerged as a practical DNN training mechanism that enables the convolution kernels to be initialized with the weights learned from the pretrained model and solves the problem of training data drawn from different distributions. TL is closely connected with DNN splitting, the goal of which is to reduce the energy cost of DNN model training on mobile devices and suitable for general-feature image recognition.

知识迁移学习（也称为 TL）已成为一种实用的 DNN 训练机制，它可以使用从预训练模型中学习的权重初始化卷积核，并解决从不同分布中提取训练数据的问题。TL 与 DNN 分裂密切相关，其目的是降低移动设备上 DNN 模型训练的能量成本，适合一般特征图像识别。

FL preserves privacy by leaving raw data on local devices and trains a shared model on the server by uploading the computed updates. Rather than transmitting the raw data, DNN splitting selects a splitting point, thereby enabling distributed DNN models to be trained using the partially processed data. TL applies the general features learned from a DNN pretrained on the basic data to a specific data set or task.

总而言之，联邦学习通过在本地设备上保留原始数据来保护隐私，并通过上传计算出的更新在服务器上训练共享模型。分裂学习不传输原始数据，而是选择一个分割点，从而使分布式 DNN 模型能够使用部分处理的数据进行训练。迁移学习将从对基本数据进行预训练的 DNN 中学习到的一般特性应用于特定的数据集或任务。

### Enabling Technologies for AIoT Model Training Updates

作者在本节介绍了 AIoT 模型训练的更新方法，主要从更新频率和更新大小两个角度切入进行阐述。

#### Frequency of Training Updates

In distributed DL training, a locally trained model or preprocessed data must be uploaded to a central server. One important issue is to optimize the gradient of the shared model through the gradient updates on end devices.

在分布式深度学习训练中，必须将本地训练的模型或预处理的数据上载到中央服务器。一个重要的问题是通过终端设备上的梯度更新来优化共享模型的梯度。

Stochastic gradient descent (SGD) is a widely used gradient descent method that updates the minibatch gradient over the entire data set. Generally, there are two kinds of SGD: 1) synchronous and 2) asynchronous SGD.

作者接下来详细介绍了随机梯度下降 SGD 这一广泛使用的梯度下降方法，它可以在整个数据集上更新小批量梯度。并且，SGD 分为同步和异步两种。它们的主要区别在于：

- 同步 SGD：如果所有设备都完成了计算任务，则每个设备都会在本地训练数据上使用梯度同步更新其参数。收敛结果相对更好，但由于需要等待其他设备，因此在实践中收敛速度较慢。
- 异步 SGD：只要有设备完成了计算任务，那么就立刻使用梯度同步更新全局的参数。异步 SGD 的收敛速度比同步更快，但代价是额外的噪声，并且可能导致较差的收敛结果。

FL also adopts SGD. In [169], the federated averaging (FedAvg) method for FL with a DNN established based on iterative model averaging is presented, in which end devices update the DNN model with one-step SGD and the server averages the obtained models with weights. This approach can be also applied to unbalanced and non-IID distributions.

作者还指出，联邦学习也采用 SGD 进行更新参数。相关工作提出了基于迭代模型平均的 DNN 联邦平均 FedAvg 方法，其中终端设备使用一次 SGD 更新 DNN 模型，服务器使用权重对获得的模型进行平均。这种方法也适用于不平衡和非独立同分布的数据。

#### Size of Training Updates

In addition to the factor of the frequency of training updates, the size of training updates significantly influences on the transmission bandwidth. Gradient compression is usually adopted to reduce the size of model updates communicated to the central server, which aims to compress the gradient information of the updated model.

除了训练更新频率的因素外，训练更新的大小对传输带宽也有显著影响。通常采用梯度压缩来减小传递给中央服务器的模型更新的大小，目的是压缩更新模型的梯度信息。

具体而言，作者主要总结了如下两种方法：

##### Gradient quantization: 梯度量化

Gradient quantization carries out lossy compression of the gradient vectors by using a finite-bit low-width number instead of the original floating-point gradients, which is similar to parameter quantization of inference. The difference between these methods lies in whether the quantization technique is applied to the model gradients or the model parameters.

梯度量化通过使用有限位低宽度数代替原始浮点梯度来对梯度向量进行有损压缩，这类似于推理的参数量化。这两种方法之间的区别在于量化技术是应用于模型梯度还是模型参数。

##### Gradient sparsification: 梯度稀疏化

Gradient sparsification reduces the communication costs by dropping important gradient updates and transmitting only updates that exceed a certain threshold.

梯度稀疏化通过丢弃重要的梯度更新并仅传输超过某个阈值的更新来降低通信成本。

### Security Enhancement

Distributed learning has shown a strong trend toward largescale model training in AIoT, where a server coordinates the computational power of end devices by sharing the trained data or aggregating local models trained on individual devices. This kind of method can stop privacy leaks from directly sharing the raw data collected from end devices; however, the gradient information shared by end devices still inevitably divulges private information. Thus, research and development of privacy preservation for AI model training is necessary.

分布式学习已显示出在 AIoT 中进行大规模模型训练的强大趋势，在 AIoT 中，服务器通过共享培训数据或聚合在单个设备上培训的本地模型来协调终端设备的计算能力。这种方法可以阻止隐私泄露，避免直接共享从终端设备收集的原始数据；然而，终端设备共享的梯度信息仍然不可避免地泄露私人信息。因此，研究和开发用于人工智能模型训练的隐私保护是必要的。

Generally, there are two obstacles: the first is that attackers may infer sensitive information from aggregated data or gradients; the other obstacle is that third parties are not trusted, thus causing data or model leakage.

通常，存在两个障碍：第一个障碍是攻击者可能从聚合数据或梯度推断敏感信息；另一个障碍是第三方不受信任，从而导致数据或模型泄漏。

作者主要从如下两个角度展开介绍隐私安全增强：

- Data Privacy and Security: 数据隐私安全性
- System Security: 系统安全性

## Open Challenges and Future Directions

作者认为 AIoT 中的一些开放挑战和潜在的未来方向如下：

- Heterogeneity and Interoperability: 异构性和互操作性
- Resource Management: 资源管理
- Model Inference and Training: 模型推理与训练
- Security and Privacy: 安全和隐私
- Artificial Intelligence Ethics in Artificial Intelligence of Things: AIoT 中的人工智能伦理

{{< callout type="info" >}}

本文是写得相对来说很不错的一篇综述，逻辑清晰。作者给出了人工智能、物联网、边缘计算等概念，引出边缘计算辅助 AIoT 的概念。随后作者以一个实际的 AIoT 示例介绍人工智能如何应用于实际的 IoT 场景，并且还介绍了人工智能模型在网络边缘推理和训练两方面的技术。

从整篇文章来看，本文的逻辑是从概念到应用，然后再到技术。这有一个从抽象到具体，再到抽象的过程。本文没有特别侧重概念、应用或者技术的任何一方面。本文的最大贡献在于捋清了人工智能、物联网、边缘计算等概念的关系，并对边缘智能赋能 AIoT 进行了深入阐述。

考虑到本文的篇幅和侧重点，在介绍 AIoT 相关技术时，训练和推理各项技术仅进行了简单的分类。特别是在介绍推理时，将各项技术按照终端本地推理和边缘协同推理分类存在一些问题。以模型提前退出这项技术为例，将它放到边缘协同推理是有些牵强的。因为模型提前退出是为了平衡推理时延和精度的优化，它既适用于终端本地推理，也适用于边缘协同推理。

{{< /callout >}}