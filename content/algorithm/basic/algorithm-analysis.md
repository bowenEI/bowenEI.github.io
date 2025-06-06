---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "算法分析"
linktitle: "算法分析"
date: 2021-10-16T20:49:20+08:00
type: docs
summary: ""
weight: 20
---

<!--more-->

## 算法执行效率的评估

- **经验法**：对各种算法编程，用不同实例进行实验；
- **理论法**：以数学化的方式确定算法所需要资源数与实例大小之间函数关系。

### 经验法的问题

- 依赖于计算机
- 依赖于语言/编程技能
- 需要一定的编程/调试时间
- 只能评估部分实例的效率

### 理论法的优点

- 不依赖于计算机
- 不依赖于语言/编程技能
- 节省了无谓编程时间
- 可研究任何在实例上算法效率

## 算法好坏的衡量

最初，用所需计算时间来衡量算法的好坏。但不同的机器相互之间无法比较，故需要用独立于具体计算机的客观衡量标准：

### 问题的规模

输入规模通常用 \(n\) 来表示，也可有两个以上的参数，如图中的顶点数和边数。

### 基本运算

基本运算是解决给定问题时占支配地位的运算。通常情况下，讨论一个算法优劣时，我们只讨论基本运算的执行次数。因为它是占支配地位的，而其它的运算可以忽略不计。

基本运算是算法中最为基本的运算，在伪代码中很容易识别，而且与编程语言无关。假设在每个基本运算都在RAM模型中花费一定的时间，无需精确衡量执行多少时间。

### 算法的计算量函数

$$
C = T(N, I, A)
$$

式中，\(N\) 表示问题的规模，\(I\) 表示输入，\(A\) 表示算法本身。

变量 \(A\) 可以隐去，通常研究算法在一台抽象计算机上运行所需时间。

其实变量 \(I\) 也可以隐去，因为不必研究每种合法输入的计算量，只需要考虑算法的最好情况、最坏情况和平均情况。

那么最终算法的计算量函数就可以简化为：

$$
C = T(N)
$$

## 算法的时间复杂度

用输入规模的某个函数来表示算法的基本运算量，称为算法的时间复杂度，即：

$$
C = T(N)
$$

### 复杂性渐进形态

当比较两个算法的渐近复杂性的阶不同时，只要确定各自的阶，即可判定哪个算法效率高。

- 渐近上界记号 \(O\)
- 渐进下界记号 \(\Omega\)
- 紧渐近界记号 \(\Theta\)
- 非紧上界记号 \(o\)
- 非紧下界记号 \(\omega\)

### 和的估计与界限

结合数学上的数列求和方法以及求积分的方法求解。