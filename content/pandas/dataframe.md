---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Dataframe 对象"
linktitle: "Dataframe 对象"
date: 2022-02-18T16:41:59+08:00
type: docs
summary: ""
weight: 20
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

`DataFrame` 是一种二维标记数据结构，具有可能不同类型的列。您可以将其视为电子表格或 SQL 表，或 `Series` 对象的字典。它通常是最常用的 **pandas** 对象。

除了数据，您还可以选择传递索引（行标签）和列（列标签）参数。如果您传递索引和/或列，则保证结果 `DataFrame` 的索引和/或列。因此，`Series` 的字典加上特定的索引将丢弃所有与传递的索引不匹配的数据。

## 创建 DataFrame 对象

与 `Series` 一样，`DataFrame` 接受许多不同类型的输入：

### 以 Series 或 dict 为值的 dict


```python
data = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
```

结果索引将是各种系列的索引的并集。如果有任何嵌套的 `dict`，这些将首先转换为 `Series`。如果未传递任何列，则这些列将是 `dict` 键的有序列表。


```python
pd.DataFrame(data)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, index=['d', 'b', 'a'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, index=['d', 'b', 'a'], columns=['two', 'three'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <td>4.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 以 list 或 ndarray 为值的 dict

`ndarrays` 必须都是相同的长度。如果传递了索引，它显然也必须与数组的长度相同。如果没有传递索引，则结果将是 `range(n)`，其中 `n` 是数组长度。


```python
data = {
    'one': [1.0, 2.0, 3.0, 4.0],
    'two': [4.0, 3.0, 2.0, 1.0],
}
```


```python
pd.DataFrame(data)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



### 结构化或记录数组


```python
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
data
```




    array([(0, 0., b''), (0, 0., b'')],
          dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])




```python
data[:] = [
    (1, 2.0, 'Hello'),
    (2, 3.0, 'World'),
]
data
```




    array([(1, 2., b'Hello'), (2, 3., b'World')],
          dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])




```python
pd.DataFrame(data)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2.0</td>
      <td>b'Hello'</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.0</td>
      <td>b'World'</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, index=['first', 'second'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>1</td>
      <td>2.0</td>
      <td>b'Hello'</td>
    </tr>
    <tr>
      <th>second</th>
      <td>2</td>
      <td>3.0</td>
      <td>b'World'</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, columns=['C', 'A', 'B'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'Hello'</td>
      <td>1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'World'</td>
      <td>2</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



### 由 dict 组成的 list


```python
data = [
    {'a': 1, 'b': 2},
    {'a': 5, 'b': 10, 'c': 20},
]
```


```python
pd.DataFrame(data)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>10</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, index=['first', 'second'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>second</th>
      <td>5</td>
      <td>10</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, columns=['a', 'b'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



### 以 tuple 为键的 dict

这样创建出的 `DataFrame` 具有多重索引框架。


```python
df = pd.DataFrame(
    {
        ('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
        ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
        ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
        ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
        ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10},
    }
)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>b</th>
      <th>a</th>
      <th>c</th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">A</th>
      <th>B</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>D</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



索引 `'a'` 和 `'b'` 返回的还是 DataFrame 对象，它是嵌套在 `df2` 里面的。


```python
df['a']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>b</th>
      <th>a</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">A</th>
      <th>B</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>D</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['b']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">A</th>
      <th>B</th>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>D</th>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



### namedtuple 序列

`namedtuple` 的字段名称决定了 `DataFrame` 的列。剩下的命名元组（或元组）被简单地解包，它们的值被输入到 `DataFrame` 的行中。


```python
from collections import namedtuple
Point = namedtuple('Point', 'x y')
```


```python
pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



如果这些元组中的任何一个比第一个 `namedtuple` 短，则相应行中后面的列被标记为缺失值。如果有任何比第一个命名元组长，则会引发 ValueError。


```python
Point3D = namedtuple('Point3D', 'x y z')
```


```python
pd.DataFrame([Point3D(0, 0, 0), Point3D(0, 3, 5), Point(2, 3)])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### dataclass 序列


```python
from dataclasses import make_dataclass
Point = make_dataclass('Point', [('x', int), ('y', int)])
```


```python
pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



### 备用构造函数


```python
pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



如果参数 `orient='index'`，键将是行标签。在这种情况下，您还可以传递所需的列名：


```python
pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]))
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
data
```




    array([(0, 0., b''), (0, 0., b'')],
          dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])




```python
pd.DataFrame.from_records(data, index='C')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>C</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b''</th>
      <td>0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>b''</th>
      <td>0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## DataFrame 对象的属性


```python
data = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index
```




    Index(['a', 'b', 'c', 'd'], dtype='object')




```python
df.columns
```




    Index(['one', 'two'], dtype='object')



类似 **NumPy** `ndarray`，可以对 `DataFrame` 对象进行转置：


```python
df.T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



注意：`DataFrame` 并非完全像二维 **NumPy** `ndarray` 那样工作。

## DataFrame 列操作


```python
data = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



可以在语义上认为 `DataFrame` 对象是索引 `Series` 对象的字典。因此，对 `DataFrame` 对象进行列操作和对 `dict` 对象进行增删改查等操作类似。

### 选择


```python
df['one']
```




    a    1.0
    b    2.0
    c    3.0
    d    NaN
    Name: one, dtype: float64



### 运算


```python
df['three'] = df['one'] * df['two']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['flag'] = df['one'] > 2
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



### 删除


```python
del df['two']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>three</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>4.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>9.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
three = df.pop('three')
three
```




    a    1.0
    b    4.0
    c    9.0
    d    NaN
    Name: three, dtype: float64




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



### 插入


```python
df['foo'] = 'bar'
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>flag</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>False</td>
      <td>bar</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>False</td>
      <td>bar</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>True</td>
      <td>bar</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>False</td>
      <td>bar</td>
    </tr>
  </tbody>
</table>
</div>



当插入一个与 `DataFrame` 没有相同索引的 `Series` 时，它将符合 `DataFrame` 的索引：


```python
df["one_trunc"] = df["one"][:2]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>flag</th>
      <th>foo</th>
      <th>one_trunc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>False</td>
      <td>bar</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>False</td>
      <td>bar</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>True</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>False</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



默认情况下，列在最后插入。插入函数可用于在列中的特定位置插入：


```python
df.insert(1, "bar", df["one"])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>bar</th>
      <th>flag</th>
      <th>foo</th>
      <th>one_trunc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>False</td>
      <td>bar</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>bar</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>True</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


