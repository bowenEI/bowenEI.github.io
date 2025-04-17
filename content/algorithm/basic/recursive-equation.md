---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "递归方程"
linktitle: "递归方程"
date: 2021-10-16T20:49:47+08:00
type: docs
summary: ""
weight: 30
---

<!--more-->

## 归并排序算法的递归方程

$$
\begin{aligned}
T(n) = \begin{cases}
\Theta(1) & n=1 \\
2T(\frac{n}{2})+\Theta(n) & n>1
\end{cases}
\end{aligned}
$$

这个方程的含义是如果只有 \(1\) 个元素的数组需要做归并排序，那么在常数时间内就能得到有序数组。

如果是 \(n\) 个元素的数组需要做归并排序，那么需要将问题一分为二，每个子问题各需要 \(T(\frac{n}{2})\) 的时间。解决子问题以后，当前问题转化为合并有序数组问题，两个指针会不重复扫描每个元素一遍，复杂度为 \(\Theta(n)\)。

可以使用逐层展开法和变量替换法求解 \(T(n)\)，但是比较麻烦，仅作了解即可。

## Master 定理

$$
T(n) = aT(\frac{n}{b})+f(n), a \ge 1, b > 1, f(n) > 0
$$

比较 \(n ^ {\log_{b}{a}}\) 的阶和 \(f(n)\) 的大小：

- 若 \(n ^ {\log_{b}{a}}\) 大，则 \(T(n) = \Theta(n ^ {\log_{b}{a}})\)
- 若 \(f(n)\) 大，则 \(T(n) = \Theta(f(n))\)
- 若 \(n ^ {\log_{b}{a}} = f(n)\)，则 \(T(n) = \Theta(n ^ {\log_{b}{a}} \log_{}{n}) = \Theta(f(n) \log_{}{n})\)

对于归并排序，\(a=2\)，\(b=2\)，则 \(n ^ {\log_{b}{a}} = n\)。而 \(f(n) = \Theta(n)\)，它们的阶数相当。因此归并排序的时间复杂度 \(T(n) = \Theta(n\log_{}{n})\)。

## Master 定理的证明