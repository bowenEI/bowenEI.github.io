---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "NumPy 广播机制"
linktitle: "NumPy 广播机制"
date: 2021-04-17T20:43:39+08:00
type: docs
weight: 60
summary: ""
---

<!--more-->


```python
import numpy as np
```

广播 `Broadcast` 是 **NumPy** 对不同形状 `shape` 的数组进行数值计算的方式，对数组的算术运算通常在相应的元素上进行。

一般地，如果两个数组 `a` 和 `b` 形状相同，即满足 `a.shape == b.shape`，那么 `a * b` 的结果就是 `a` 与 `b` 数组对应位相乘。这要求维数 `ndim` 相同，且各维度的长度相同，即 `shape` 元组完全相同。

而当运算中的两个数组的形状不同时，**NumPy** 将会自动触发广播机制。


```python
a = np.arange(12).reshape(3, 4)
b = np.arange(1, 4)
a, b
```




    (array([[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]]),
     array([1, 2, 3]))



下面我们直接将 `shape` 不同的 `a` 和 `b` 相加：


```python
a + b
```


    ---------------------------------------------------------------------------
    
    ValueError                                Traceback (most recent call last)
    
    <ipython-input-3-bd58363a63fc> in <module>
    ----> 1 a + b


    ValueError: operands could not be broadcast together with shapes (3,4) (3,) 


出现了异常，提示 `(3, 4)` 和 `(3,)` 两个 `shape` 不能直接相加。

我们可以尝试对只有 1 个维度的数组 `b` 扩展到 2 个维度：


```python
b = b.reshape(3, 1)
b
```




    array([[1],
           [2],
           [3]])



这样就可以直接相加了：


```python
a + b
```




    array([[ 1,  2,  3,  4],
           [ 6,  7,  8,  9],
           [11, 12, 13, 14]])



现在，我们有如下数组：


```python
c = np.arange(4)
c
```




    array([0, 1, 2, 3])



我们继续进行加法运算：


```python
a + c
```




    array([[ 0,  2,  4,  6],
           [ 4,  6,  8, 10],
           [ 8, 10, 12, 14]])



没有任何异常发生，这是什么原因呢？

原因在于 `shape` 的看齐机制。`a` 的 `shape` 为 `(3, 4)`，`c` 的 `shape` 为 `(4,)`。看齐的时候从 `shape` 元组的最右边进行比较（这很类似于加减法从个位开始算），只要完全相等就继续比较，直到比较完成（此时即为两个形状完全相同的数组）或者有一方维数 `ndim` 不够（维数不够的一方需要广播）才停止。

正是由于看齐机制，`a` 和 `c` 第一趟比较时发现 `shape` 都是 4，因此继续比较，结果 `c` 的维数不够，停止比较，于是 `c` 需要广播自己才能和 `a` 相加，而这在 **NumPy** 中是自动完成的。

而上一个例子中，`a` 和 `b` 的第一趟比较就因为 \(3 \ne 4\) 而出错，触发了 `shape` 不匹配的异常。

**Broadcast 机制总结如下：**

- 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
- 输出数组的形状是输入数组形状的各个维度上的最大值。
- 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
- 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。
