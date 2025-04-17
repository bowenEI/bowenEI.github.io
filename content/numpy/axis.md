---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "NumPy axis 参数"
linktitle: "NumPy axis 参数"
date: 2021-04-17T20:02:02+08:00
type: docs
weight: 50
summary: ""
---

<!--more-->


```python
import numpy as np
```

## 深入理解 axis

`axis` 的英文含义为轴，它在 **NumPy** 中是许多函数的一个重要参数。这些函数往往都支持复杂的多维数组汇总运算，`axis` 的值决定了程序员可以对高维矩阵的任何一维做汇总运算。

这个参数取名为轴是相当形象的。下面这个简单的例子就能很好地帮助我们理解这个参数为什么叫做 `axis`。


```python
Z = np.arange(12).reshape(4, 3)
Z
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [ 9, 10, 11]])



我们设置 `axis=0`，发现每一列的平均值被求解出来排成了一行：


```python
np.mean(Z, axis=0)
```




    array([4.5, 5.5, 6.5])



我们设置 `axis=1`，发现每一行的平均值被求解出来排成了一行：


```python
np.mean(Z, axis=1)
```




    array([ 1.,  4.,  7., 10.])



上面的程序段首先定义了一个大小为 16 的一维数组并将之打包成 \(4 \times 4\) 矩阵，参数 `axis` 先后分别设置为 0 和 1。观察输出结果可知：第一次是求出了每列的平均值，第二次是求出了每行的平均值。

由此，我们可以得出一个初步的结论：`axis=1` 是对矩阵的行汇总，`axis=0` 是对矩阵的列汇总。这个过程和 Excel 中的一些公式和函数的功能很相近，特别是和其中的分类汇总功能很相近。`axis` 确实就是一个轴，它在矩阵中平移（在垂直轴方向上分类），所到之处沿平行轴方向汇总。

例如当 `axis=1` 时，说明要在 `index=1` 的列那一维上做汇总操作。此时的轴一定是水平的，因为在平行轴方向 `axis` 所表示的那一维是变化的，是要对整个域汇总的。相应地，会在另一维（行）上遍历。所得数组一定是降低了一维变成了一维数组。

按照这个运算法则，可以将之推广到多维数组。这个时候的数组不能简单表示成一维向量或者二维矩阵的形式了，只能线性地用括号匹配原则表示。但是 `axis` 的含义没有本质区别，可以总结为一句话：设 `axis=i`，则 **NumPy** 沿着第 `i` 个下标变化的方向进行汇总操作。下面是一个三维的例子：


```python
Z = np.arange(24).reshape(2, 3, 4)
Z
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])



我们设置 `axis=0`，发现大小为 2 的那一维被汇总了，只剩下 \(3 \times 4\) 矩阵。


```python
np.mean(Z, axis=0)
```




    array([[ 6.,  7.,  8.,  9.],
           [10., 11., 12., 13.],
           [14., 15., 16., 17.]])



我们设置 `axis=1`，发现大小为 3 的那一维被汇总了，只剩下 \(2 \times 4\) 矩阵。


```python
np.mean(Z, axis=1)
```




    array([[ 4.,  5.,  6.,  7.],
           [16., 17., 18., 19.]])



我们设置 `axis=2`，发现大小为 4 的那一维被汇总了，只剩下 \(2 \times 3\) 矩阵。


```python
np.mean(Z, axis=2)
```




    array([[ 1.5,  5.5,  9.5],
           [13.5, 17.5, 21.5]])



## NumPy 统计函数

**NumPy** 统计函数经常涉及到 axis 参数的使用。


```python
A = np.arange(12).reshape(3, 4)
A
```




    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])



### 求和


```python
np.sum(A, axis=0)
```




    array([12, 15, 18, 21])




```python
np.sum(A, axis=1)
```




    array([ 6, 22, 38])



### 平均数


```python
np.mean(A, axis=0)
```




    array([4., 5., 6., 7.])




```python
np.mean(A, axis=1)
```




    array([1.5, 5.5, 9.5])



`np.average` 专门用于求解加权平均数，`w` 为权重矩阵。


```python
w = np.random.randint(1, 10, size=(3, 4))
w
```




    array([[2, 7, 3, 5],
           [7, 4, 5, 3],
           [2, 4, 2, 7]])




```python
np.average(A, axis=0, weights=w)
```




    array([4.        , 4.2       , 5.6       , 7.53333333])




```python
np.average(A, axis=1, weights=w)
```




    array([1.64705882, 5.21052632, 9.93333333])



### 方差与标准差

方差


```python
np.var(A, axis=0)
```




    array([10.66666667, 10.66666667, 10.66666667, 10.66666667])




```python
np.var(A, axis=1)
```




    array([1.25, 1.25, 1.25])



标准差


```python
np.std(A, axis=0)
```




    array([3.26598632, 3.26598632, 3.26598632, 3.26598632])




```python
np.std(A, axis=1)
```




    array([1.11803399, 1.11803399, 1.11803399])



### 不支持 axis 参数的统计函数

最大值（最小值）


```python
np.max(A)
```




    11




```python
np.min(A)
```




    0



最大值（最小值）索引


```python
np.argmax(A)
```




    11




```python
np.argmin(A)
```




    0



极差，即最大值与最小值之差


```python
np.ptp(A)
```




    11



中位数


```python
np.median(A)
```




    5.5



## axis 参数的应用

### 拼接两个矩阵


```python
x = np.arange(9).reshape(3, 3)
y = np.arange(-3, 6).reshape(3, 3)
x, y
```




    (array([[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]),
     array([[-3, -2, -1],
            [ 0,  1,  2],
            [ 3,  4,  5]]))




```python
np.concatenate((x, y), axis=0)
```




    array([[ 0,  1,  2],
           [ 3,  4,  5],
           [ 6,  7,  8],
           [-3, -2, -1],
           [ 0,  1,  2],
           [ 3,  4,  5]])




```python
np.concatenate((x, y), axis=1)
```




    array([[ 0,  1,  2, -3, -2, -1],
           [ 3,  4,  5,  0,  1,  2],
           [ 6,  7,  8,  3,  4,  5]])


