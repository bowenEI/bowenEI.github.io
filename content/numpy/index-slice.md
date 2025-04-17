---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "NumPy 索引与切片"
linktitle: "NumPy 索引与切片"
date: 2021-04-17T17:31:38+08:00
type: docs
weight: 20
summary: ""
---

<!--more-->


```python
import numpy as np
```


```python
A = np.arange(24).reshape((2, 3, 4))
A
```




    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])



## 索引

下标从 0 开始。


```python
A[1, 2, 3]
```




    23



负数索引表示从后向前数，-1 表示最后一个元素的下标，以此类推。


```python
A[-1, -2, -3]
```




    17



## 切片

冒号表达式：`begin:end:step`，提取范围为 \([begin, end)\)，步长为 \(step\)。


```python
A[1, 1:2, 1:3]
```




    array([[17, 18]])



可以只给出 `begin` 或 `end`，表示从 `begin` 到尾（从头到 `end`）：


```python
A[1, 1:, :2]
```




    array([[16, 17],
           [20, 21]])



只有一个冒号表示这一维全部提取：


```python
A[:, 1, 1]
```




    array([ 5, 17])



省略号可以省略多个维度连续的冒号：


```python
A[..., 0]
```




    array([[ 0,  4,  8],
           [12, 16, 20]])



冒号表达式可以省略开始和结束的位置，只给出步长：


```python
A[:, ::2, :]
```




    array([[[ 0,  1,  2,  3],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [20, 21, 22, 23]]])


