---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Series 对象"
linktitle: "Series 对象"
date: 2022-02-18T15:01:52+08:00
type: docs
summary: ""
weight: 10
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

`Series` 是一个带标签的一维数组，能够保存任何数据类型（整数、字符串、浮点数、Python 对象等）。轴 `axis` 标签统称为索引 `index`。

## 创建 Series 对象

创建 `Serires` 对象需要提供 `data` 和 `index` 两个参数。其中 `index` 是需要传入的索引，即轴标签列表。因此，根据数据类型可以分为如下几种情况：

### ndarray

如果 `data` 是 `ndarray`，则 `index` 必须与 `data` 的长度相同。


```python
pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
```




    a   -0.247457
    b    0.127203
    c    0.048504
    d   -1.802860
    e   -1.480528
    dtype: float64



如果没有传递索引，则将创建一个具有值 `[0, ..., len(data) - 1]` 的索引。


```python
pd.Series(np.random.randn(5))
```




    0   -0.218089
    1   -1.875552
    2   -0.351250
    3    2.237674
    4    0.794604
    dtype: float64



### dict


```python
pd.Series({'b': 1, 'a': 0, 'c': 2})
```




    b    1
    a    0
    c    2
    dtype: int64



### 标量值

如果数据是标量值，则必须提供索引。该值将重复以匹配索引的长度。


```python
pd.Series(5.0, index=['a', 'b', 'c', 'd', 'e'])
```




    a    5.0
    b    5.0
    c    5.0
    d    5.0
    e    5.0
    dtype: float64



## Series 类似 ndarray

`Series` 的行为与 `ndarray` 非常相似，并且是大多数 **NumPy** 函数的有效参数。

### 索引和切片

注意：切片等操作也会对索引进行切片。


```python
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
s
```




    a    1.234485
    b   -0.893518
    c    0.400802
    d   -1.328360
    e   -1.023169
    dtype: float64




```python
s[0]
```

    C:\Users\Fourier\AppData\Local\Temp\ipykernel_17908\243613605.py:1: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
      s[0]
    




    1.2344849322112634




```python
s[:3]
```




    a    1.234485
    b   -0.893518
    c    0.400802
    dtype: float64



### 矩阵索引


```python
s[s > s.median()]
```




    a    1.234485
    c    0.400802
    dtype: float64



### 数学运算


```python
np.exp(s)
```




    a    3.436608
    b    0.409214
    c    1.493022
    d    0.264911
    e    0.359454
    dtype: float64



### ndarry 属性


```python
s.array
```




    <NumpyExtensionArray>
    [ 1.2344849322112634, -0.8935181616923943, 0.40080196379724387,
     -1.3283596009432421,  -1.023169455667722]
    Length: 5, dtype: float64




```python
s.dtype
```




    dtype('float64')



### 强制类型转换


```python
s.to_numpy()
```




    array([ 1.23448493, -0.89351816,  0.40080196, -1.3283596 , -1.02316946])



## Series 类似 dict

`Series` 就像一个固定大小的 `dict`，可以通过索引标签获取和设置值：


```python
s['a']
```




    1.2344849322112634




```python
s['e'] = 12.0
s
```




    a     1.234485
    b    -0.893518
    c     0.400802
    d    -1.328360
    e    12.000000
    dtype: float64




```python
'e' in s, 'f' in s
```




    (True, False)



如果未包含标签，会抛出异常：


```python
try:
    s['f']
except KeyError:
    print('KeyError')
```

    KeyError
    

使用 `get` 方法，缺少的标签将返回 `None` 或指定的默认值：


```python
s.get('f')
```


```python
s.get('f', np.nan)
```




    nan



## 向量化操作和标签对齐

使用原始 **NumPy** 数组时，通常不需要逐个值循环。在 **pandas** 中使用 `Series` 时也是如此。`Series` 也可以传递给大多数需要 `ndarray` 的 **NumPy** 方法。


```python
s + s
```




    a     2.468970
    b    -1.787036
    c     0.801604
    d    -2.656719
    e    24.000000
    dtype: float64




```python
s * 2
```




    a     2.468970
    b    -1.787036
    c     0.801604
    d    -2.656719
    e    24.000000
    dtype: float64



`Series` 和 `ndarray` 之间的一个关键区别是 `Series` 之间的操作会根据标签自动对齐数据。因此，您可以编写计算而不考虑所涉及的系列是否具有相同的标签。


```python
s[1:] + s[:-1]
```




    a         NaN
    b   -1.787036
    c    0.801604
    d   -2.656719
    e         NaN
    dtype: float64



未对齐系列之间的操作结果将包含所涉及的索引的并集。如果在一个系列或另一个系列中找不到标签，则结果将被标记为缺失 `NaN`。

## name 属性


```python
s = pd.Series(np.random.randn(5), name="something")
s
```




    0    0.715769
    1   -0.089104
    2    1.187363
    3   -1.413279
    4    0.272194
    Name: something, dtype: float64




```python
s.name
```




    'something'



在许多情况下，`Series` 名称将自动分配，特别是在获取 `DataFrame` 的一维切片时。详见 `DataFrame` 章节。


```python
new_s = s.rename('different')
new_s.name
```




    'different'



请注意，`s` 和 `new_s` 指的是不同的对象。
