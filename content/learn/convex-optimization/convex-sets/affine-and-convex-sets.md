---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "仿射集合和凸集"
linktitle: "仿射集合和凸集"
date: 2021-11-30T14:34:47+08:00
type: book
summary: ""
weight: 110
---

<!--more-->

## 直线与线段

设 $x_1 \ne x_2$ 为 $\mathbf{R}^n$ 空间中的两个点，那么

\begin{align}
y = \theta x_1 + (1-\theta) x_2, \quad \theta \in \mathbf{R}
\end{align}

组成一条穿越 $x_1$ 和 $x_2$ 的**直线**；

\begin{align}
y = \theta x_1 + (1-\theta) x_2, \quad \theta \in [0, 1]
\end{align}

构成了 $x_1$ 和 $x_2$ 之间的（闭）**线段**。

还有如下一种表示形式，它类似于直线的参数方程：

\begin{align}
y = x_2 + \theta(x_1 - x_2)
\end{align}

## 仿射集合

如果通过集合 $C \subseteq \mathbf{R}^{n}$ 中任意两个不同点的直线仍然在集合 $C$ 中，那么称集合 $C$ 是**仿射**的，即

\begin{align}
\forall x_1,x_2 \in C, \quad \theta x_1 + (1 - \theta) x_2 \in C \quad (\theta \in \mathbf{R})
\end{align}

这个概念可以推广至多个点的情况：如果 $\theta_1 + \cdots + \theta_k = 1$，那么称 $\theta_1 x_1 + \cdots + \theta_k x_k$ 为 $x_1, \cdots, x_k$ 的**仿射组合**。如果一个集合中的任意两点的仿射组合仍在该集合中，那么称该集合为**仿射集合**。

设 $V$ 是一个子空间（即关于加法和数乘运算是封闭的），则仿射集合 $C$ 可以表示为

\begin{align}
C = V + x_0 = \\{v + x_0 \mid v \in V\\}
\end{align}

与仿射集合 $C$ 相关联的子空间 $V$ 与 $x_0$ 的选取无关，所以 $x_0$ 可以是 $C$ 中的任意一点。

我们称由集合 $C \subseteq \mathbf{R}^{n}$ 中的点的所有仿射组合组成的集合为 $C$ 的**仿射包**，即

\begin{align}
\operatorname{aff} C = \\{\theta_1 x_1 + \cdots + \theta_1 x_1 \mid x_1, \cdots, x_k \in C, \theta_1 + \cdots + \theta_k = 1\\}
\end{align}

仿射包是包含 $C$ 的最小的仿射集合。

## 仿射维数与相对内部

集合 $C$ 的**仿射维数** 为其仿射包的维数。例如，$\mathbf{R}^{2}$ 上的单位圆环 $\\{x \in \mathbf{R}^{2} \mid x_1^2+x_2^2=1\\}$ 的仿射包是全空间 $\mathbf{R}^{2}$，故其仿射维数为 $2$。

考虑 $\mathbf{R}^{3}$ 中处于 $(x_1,x_2)$ 平面的一个正方形，定义

\begin{align}
C = \\{x \in \mathbf{R}^{3} \mid -1 \leqslant x_1 \leqslant 1, -1 \leqslant x_2 \leqslant 1, x_3=0\\}
\end{align}

其仿射包为 $x_1, x_2$ 平面，即 $\operatorname{aff}C = \\{x \in \mathbf{R}^{3} \mid x_3=0\\}$。$C$ 的仿射维数小于 $3$，其相对内部为

\begin{align}
\operatorname{relint} C = \\{x \in \mathbf{R}^{3} \mid -1 < x_1 < 1, -1 < x_2 < 1, x_3=0\\}
\end{align}

$C$ 在 $\mathbf{R}^{3}$ 中的边界是其自身，而相对边界是其边框，即

\begin{align}
\operatorname{cl} C \backslash \operatorname{relint} C = \\{x \in \mathbf{R}^{3} \mid \max \\{\left|x_1\right|, \left|x_2\right|\\}, x_3=0\\}
\end{align}

## 凸集

若对 $\forall x_1, x_2 \in C$ 和对 $\forall \theta \in [0, 1]$，都有

\begin{align}
\theta x_1 + (1 - \theta) x_2 \in C
\end{align}

则称集合 $C$ 为**凸集**。

{{< callout note >}}

**仿射集合是凸集**

由于仿射集包含穿过集合中任意不同两点的整条直线，任意不同两点间的线段自然也在集合中，因而仿射集是凸集。

{{< /callout >}}

{{< figure src="learn/convex-optimization/convex-sets/2-1-1.png" >}}

如图所示，黄色的正六边形是凸集；蓝色的圆环不是凸集，因为任意两点之间的连线不一定都被集合包含；绿色的正方形也不是凸集，因为它仅包含部分边界。

我们称 $\theta_1 x_1 + \cdots + \theta_1 x_1$ 为点 $x_1, \cdots, x_k$ 的一个**凸组合**，其中 $\theta_1 + \cdots + \theta_k = 1$ 并且 $\theta_i \geqslant 0, i = 1, \cdots, k$。可以将点的图组合理解为他们的混合或加权平均，$\theta_i$ 代表混合时 $x_i$ 所占的份数。

我们称集合 $C$ 中所有点的凸组合的集合为其**凸包**，即

\begin{align}
\operatorname{conv} C=\\{\theta_1 x_1+\cdots+\theta_k x_k \mid x_i \in C, \theta_i \geqslant 0, \\\\ i=1, \cdots, k, \theta_1+\cdots+\theta_k=1\\}
\end{align}

{{< figure src="learn/convex-optimization/convex-sets/2-1-2.png" >}}

如图所示，圆环的闭包是整个圆。

凸组合的概念可以扩展到无穷级数、积分以及大多数形式的概率分布。例如：

\begin{align}
\sum_{i=1}^{\infty} \theta_{i}=1 &\Rightarrow \sum_{i=1}^{\infty} \theta_{i} x_{i} \in C \\\\
\int_{C} p(x) d x =1 &\Rightarrow \int_{C} p(x) x d x \in C
\end{align}

## 锥

如果对 $\forall x \in C$ 和 $\forall \theta \geqslant 0$ 都有 $\theta x \in C$，那么我们称集合 $C$ 是**锥**或者**非负齐次**。若集合 $C$ 是锥并且是凸的，则称 $C$ 为**凸锥**，即对 $\forall x_1, x_2 \in C$ 和 $\forall \theta_1, \theta_2 \geqslant 0$，都有

\begin{align}
\theta_1 x_1 + \theta_2 x_2 \in C
\end{align}

半径为 $\infty$ 的扇形和母线长为 $\infty$ 的圆锥面是典型的凸锥。

和凸组合和凸包类似，可以定义锥组合和锥包。集合 $C$ 的锥包是 $C$ 中元素的所有锥组合的集合，如图所示：

{{< figure src="learn/convex-optimization/convex-sets/2-1-3.png" >}}

## 小结

|                仿射集                 |                 凸集                  |          锥          |                凸锥                 |
| :-----------------------------------: | :-----------------------------------: | :------------------: | :---------------------------------: |
| $\theta x_1 + (1 - \theta) x_2 \in C$ | $\theta x_1 + (1 - \theta) x_2 \in C$ |   $\theta x \in C$   | $\theta_1 x_1 + \theta_2 x_2 \in C$ |
|        $\theta \in \mathbf{R}$        |          $\theta \in [0, 1]$          | $\theta \geqslant 0$ |  $\theta_1, \theta_2 \geqslant 0$   |

|                仿射组合                |                  凸组合                  |                  锥组合                  |
| :------------------------------------: | :--------------------------------------: | :--------------------------------------: |
| $\theta_1 x_1 + \cdots + \theta_k x_k$ |  $\theta_1 x_1 + \cdots + \theta_k x_k$  |  $\theta_1 x_1 + \cdots + \theta_k x_k$  |
|   $\theta_1 + \cdots + \theta_k = 1$   |    $\theta_1 + \cdots + \theta_k = 1$    |                                          |
|                                        | $\theta_i \geqslant 0, i = 1, \cdots, k$ | $\theta_i \geqslant 0, i = 1, \cdots, k$ |

|               仿射包               |                   凸包                   |                   锥包                   |
| :--------------------------------: | :--------------------------------------: | :--------------------------------------: |
| $\theta_1 + \cdots + \theta_k = 1$ |    $\theta_1 + \cdots + \theta_k = 1$    |                                          |
|                                    | $\theta_i \geqslant 0, i = 1, \cdots, k$ | $\theta_i \geqslant 0, i = 1, \cdots, k$ |

