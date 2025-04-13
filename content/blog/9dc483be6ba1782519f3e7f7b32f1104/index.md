---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "调和级数的前 $n$ 项和"
subtitle: ""
summary: ""
authors: []
tags: [数学, 无穷级数, 微积分]
categories: [Knowledge]
date: 2023-12-02T23:37:55+08:00
lastmod: 2023-12-02T23:37:55+08:00
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

在推导大模型 Decoder 的自注意力的算术强度时，遇到了如下的数列求和问题：

$$
\begin{align*}
    & \sum_{i=1}^{S_{out}} \frac{1}{S_{in}+i} \\
    =\ & \sum_{i=1}^{S_{out}} \frac{1}{i} - \sum_{i=1}^{S_{in}} \frac{1}{i} \\
\end{align*}
$$

这涉及到求调和级数的前 $n$ 项和。所以，本文来研究这个问题。

<!--more-->

## 调和级数的敛散性

我们知道，$p$-级数具有如下敛散性

$$
\begin{align*}
    \sum_{n=1}^{\infty} \frac{1}{n^p} \begin{cases}
        \ \text{发散}, & p \leqslant 1 \\
        \ \text{收敛}, & p>1 
    \end{cases}
\end{align*}
$$

当 $p=1$ 时，原级数即为调和级数

$$
\begin{align*}
    \sum_{n=1}^{\infty} \frac{1}{n}
\end{align*}
$$

为了求出调和级数的前 $n$ 项和，我们需要构造和函数

$$
\begin{align*}
    f_{n}(x) &= \sum_{k=1}^{n} \frac{x^k}{k} \\
\end{align*}
$$

将调和级数表示成幂级数 $f_{n}(x)$ 在 $x=1$ 处的函数值 $f_{n}(1)$。首先对 $f_{n}(x)$ 求一阶导数

$$
\begin{align*}
    f_{n}^{\prime}(x) &= \sum_{k=1}^{n} x^{k-1} \\
    &= \frac{1-x^{n}}{1-x}
\end{align*}
$$

两边积分，得到

$$
\begin{align*}
    f_{n}(x) &= \int \frac{1-x^{n}}{1-x} \mathrm{d}x \\
    \Longrightarrow f_n(1) &= \int_{0}^{1} \frac{1-x^{n}}{1-x} \mathrm{d}x + f_{n}(0) \\
    &= \int_{0}^{1} \frac{1-x^{n}}{1-x} \mathrm{d}x \\
\end{align*}
$$

求解上述定积分需要借助 Gamma 函数和 Digamma 函数。

## Gamma 函数和 Digamma 函数

我们知道，Gamma 函数的定义最初是为了快速计算阶乘的值。它满足

$$
\Gamma(x) = x \Gamma(x-1)
$$

欧拉给出了 Gamma 函数的积分定义形式

$$
\begin{align*}
    \Gamma(x) &= \int_{0}^{+\infty} t^{x-1} e^{-t} \mathrm{d}t \\
\end{align*}
$$

Gamma 函数也被称为第二类欧拉积分。而 Digamma 函数的定义为伽玛函数的对数的导数，即

$$
\begin{align*}
    \Psi(x) &= \frac{\mathrm{d\ln{\Gamma(x)}}}{\mathrm{d}x} \\
    &= \frac{\Gamma^{\prime}(x)}{\Gamma(x)}
\end{align*}
$$

对 Gamma 函数求导，有

$$
\begin{align*}
    \Gamma^{\prime}(x) &= \frac{\mathrm{d}}{\mathrm{d}x} \int_{0}^{+\infty} t^{x-1} e^{-t} \mathrm{d}t \\
    &= \int_{0}^{+\infty} t^{x-1} e^{-t} \ln{t} \mathrm{d}t \\
    \Longrightarrow \Gamma^{\prime}(1) &= \int_{0}^{+\infty} e^{-t} \ln{t} \mathrm{d}t \\
    &= \int_{0}^{1} e^{-t} \ln{t} \mathrm{d}t + \int_{1}^{+\infty} e^{-t} \ln{t} \mathrm{d}t \\
    &= \int_{0}^{1} \frac{e^{-t}-1}{t} \mathrm{d}t + \int_{1}^{+\infty} \frac{e^{-t}}{t} \mathrm{d}t \\
    &= -\lim_{n \to \infty} \left(
        \sum_{k=1}^{n} \frac{1}{k} - \ln{n}
    \right)
\end{align*}
$$

这里省略了中间非常复杂的计算。不过，最终我们得到了一个极限，其中恰好包含调和级数和对数函数。如果能够证明这个极限收敛，就能求出调和级数的前 $n$ 项和。

## 调和级数与对数函数的关系

首先给出结论：虽然调和级数以及极限

$$
\begin{align*}
    \lim_{n \to \infty} \ln{n}
\end{align*}
$$

都发散，但是它们的差

$$
\begin{align*}
    \gamma &= \lim_{n \to \infty} \gamma_{n} \\
    &= \lim_{n \to \infty} \left( \sum_{k=1}^{n} \frac{1}{k} - \ln{n} \right)
\end{align*}
$$

收敛。通过 $\gamma_{n}$ 单调递减且有下界，可以证明这个极限存在。我们可以通过计算机求解出这个近似值为

$$
\begin{align*}
  \gamma \approx 0.5772156649
\end{align*}
$$

它被称作欧拉常数。目前，尚不能证明欧拉常数是有理数还是无理数。

这同时也说明了，调和级数和对数函数是同阶无穷大，即当 $n \to \infty$ 时

$$
\begin{align*}
    \sum_{k=1}^{n} \frac{1}{k} \sim \ln{n}
\end{align*}
$$

至此，其实我们可以估算调和级数的前 $n$ 项和为

$$
\begin{align*}
    \sum_{k=1}^{n} \frac{1}{k} \approx \ln{n} + \gamma
\end{align*}
$$

并且可以证明

$$
\begin{align*}
    \ln{(n+1)} < \sum_{k=1}^{n} \frac{1}{k} < \ln{n} + 1
\end{align*}
$$

## Digamma 函数的积分形式

有了欧拉常数 $\gamma$，通过一系列推导，可以得到 Digamma 函数的积分形式

$$
\begin{align*}
    \Psi(x) &= -\gamma + \int_{0}^{1} \frac{1-t^{x-1}}{1-t} \mathrm{d}t 
\end{align*}
$$

做好了上述铺垫后，我们就可以用 Digamma 函数来计算调和级数的前 $n$ 项和

$$
\begin{align*}
    \sum_{k=1}^{n} \frac{1}{n} &= f_{n}(1) \\
    &= \int_{0}^{1} \frac{1-t^{n}}{1-x} \mathrm{d}x \\
    &= \Psi(n+1) + \gamma
\end{align*}
$$
