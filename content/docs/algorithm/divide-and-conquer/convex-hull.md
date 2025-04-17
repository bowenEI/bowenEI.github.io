---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "寻找凸包"
linktitle: "寻找凸包"
date: 2021-10-16T20:54:43+08:00
type: docs
summary: ""
weight: 170
---

<!--more-->

## 问题描述

给定平面上 \(n\) 个点的集合 \(Q\)，\(Q\) 的凸包是一个凸多边形 \(P\)。\(Q\) 的点或者在 \(P\) 上或者在 \(P\) 内，并且连接 \(P\) 内任意两点的边都在 \(P\) 内。现在要求 \(Q\) 的凸包 \(P\)。

## 问题分析

Graham-scan 的基本思想：

- 找到最下最左顶点，其他顶点与它连线。
- 按夹角从小到大排序。
- 夹角最小的开始，寻找凸包点。

{{< figure src="/learn/algorithm/divide-and-conquer/寻找凸包1.png" >}}

是否存在分治的方法？

- 取两极端点，最右最下点 \(p_{dr}\) 和最左最上点 \(p_{ul}\)。
- 有向线 \(p_{dr}p_{ul}\) 将整个凸包被划分为右凸包和左凸包。
- 对右凸包和左凸包分别进行递归。

{{< figure src="/learn/algorithm/divide-and-conquer/寻找凸包2.png" >}}

## 算法分析

- 时间复杂度：\(O(n \log {n})\)