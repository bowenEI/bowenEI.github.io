---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "快速傅里叶变换"
linktitle: "快速傅里叶变换"
date: 2021-10-16T20:54:36+08:00
type: docs
summary: ""
weight: 160
---

<!--more-->

## 傅立叶变换

### 傅里叶变换的直观概念

任何波形可由多个正弦波叠加近似。

- 输入为长度为 \(n\) 的离散信号序列（\(n\) 一般为 \(2^k\)）
- 输出为一系列频率上的振幅和相位

### 离散傅里叶变换

性质：

- \(\omega_{n}^{2k} = \omega_{n/2}^{k}\)
- \(\omega_{n}^{n/2} = -1\)

## 快速傅里叶变换 FFT

利用离散傅里叶变换的性质，可以设计一个快速傅里叶变换的分治算法，将原问题一分为二。

## 算法分析

- 时间复杂度：\(T(n) = O(n \log {n})\)