---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "索引和选择"
linktitle: "索引和选择"
date: 2022-02-19T11:14:00+08:00
type: docs
summary: ""
weight: 30
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

## 概述

**pandas** 索引和选择的操作主要是以下五种：

| 操作               | 语法            | Result    |
| :----------------: | :-------------: | :-------: |
| 选择列             | `df[col]`       | Series    |
| 通过标签选择行     | `df.loc[label]` | Series    |
| 通过整数下标选择行 | `df.iloc[loc]`  | Series    |
| 行切片             | `df[5:10]`      | DataFrame |
| 通过布尔向量切片   | `df[bool_vec]`  | DataFrame |


```python
df = pd.DataFrame(np.random.randn(4, 5), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D', 'E'])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.103212</td>
      <td>-0.719843</td>
      <td>-0.355287</td>
      <td>-0.440257</td>
      <td>1.083105</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.215091</td>
      <td>0.350809</td>
      <td>1.129627</td>
      <td>0.179248</td>
      <td>-0.367324</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.703286</td>
      <td>0.733214</td>
      <td>-1.472511</td>
      <td>1.311112</td>
      <td>-0.663189</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.644637</td>
      <td>0.739376</td>
      <td>1.270120</td>
      <td>-1.353912</td>
      <td>0.187226</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['B']
```




    a   -0.719843
    b    0.350809
    c    0.733214
    d    0.739376
    Name: B, dtype: float64




```python
df[['B', 'C']]
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
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.719843</td>
      <td>-0.355287</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.350809</td>
      <td>1.129627</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.733214</td>
      <td>-1.472511</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.739376</td>
      <td>1.270120</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['d']
```




    A    0.644637
    B    0.739376
    C    1.270120
    D   -1.353912
    E    0.187226
    Name: d, dtype: float64




```python
df.iloc[0]
```




    A   -0.103212
    B   -0.719843
    C   -0.355287
    D   -0.440257
    E    1.083105
    Name: a, dtype: float64




```python
df[:-1]
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
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.103212</td>
      <td>-0.719843</td>
      <td>-0.355287</td>
      <td>-0.440257</td>
      <td>1.083105</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.215091</td>
      <td>0.350809</td>
      <td>1.129627</td>
      <td>0.179248</td>
      <td>-0.367324</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.703286</td>
      <td>0.733214</td>
      <td>-1.472511</td>
      <td>1.311112</td>
      <td>-0.663189</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[:2] > 0
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
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>b</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df < 0] = 0
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.083105</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.215091</td>
      <td>0.350809</td>
      <td>1.129627</td>
      <td>0.179248</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.703286</td>
      <td>0.733214</td>
      <td>0.000000</td>
      <td>1.311112</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.644637</td>
      <td>0.739376</td>
      <td>1.270120</td>
      <td>0.000000</td>
      <td>0.187226</td>
    </tr>
  </tbody>
</table>
</div>



## 使用 [] 进行索引

使用 `[]` 进行索引，实际上就是选择低维切片。对于 Series 对象和 DataFrame 对象，`[]` 返回的类型不同。

| 对象类型  | 调用方法         | 返回值类型                 |
| :-------: | :--------------: | :------------------------: |
| Series    | `series[label]`  | 标量值                     |
| DataFrame | `frame[colname]` | 对应 `colname` 的 `Series` |


```python
dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4),
                  index=dates, columns=['A', 'B', 'C', 'D'])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.169225</td>
      <td>-0.158166</td>
      <td>-0.166857</td>
      <td>-0.078189</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.584719</td>
      <td>0.631690</td>
      <td>0.001675</td>
      <td>0.263198</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.234786</td>
      <td>-1.622012</td>
      <td>-0.705652</td>
      <td>-0.171561</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>1.038103</td>
      <td>-1.316517</td>
      <td>-0.135135</td>
      <td>-0.411320</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.123070</td>
      <td>0.290033</td>
      <td>-0.372262</td>
      <td>-0.340214</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.900263</td>
      <td>0.304163</td>
      <td>-1.663322</td>
      <td>0.633026</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.766208</td>
      <td>0.359713</td>
      <td>-0.460340</td>
      <td>0.746346</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.864615</td>
      <td>-0.576092</td>
      <td>0.065375</td>
      <td>-1.200949</td>
    </tr>
  </tbody>
</table>
</div>




```python
s = df['A']
s
```




    2000-01-01    0.169225
    2000-01-02    0.584719
    2000-01-03   -0.234786
    2000-01-04    1.038103
    2000-01-05    1.123070
    2000-01-06    0.900263
    2000-01-07    0.766208
    2000-01-08    0.864615
    Freq: D, Name: A, dtype: float64




```python
s[dates[5]]
```




    0.9002627651374207



交换 `A` 和 `B` 两列：


```python
df[['B', 'A']] = df[['A', 'B']]
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.158166</td>
      <td>0.169225</td>
      <td>-0.166857</td>
      <td>-0.078189</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.631690</td>
      <td>0.584719</td>
      <td>0.001675</td>
      <td>0.263198</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-1.622012</td>
      <td>-0.234786</td>
      <td>-0.705652</td>
      <td>-0.171561</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-1.316517</td>
      <td>1.038103</td>
      <td>-0.135135</td>
      <td>-0.411320</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.290033</td>
      <td>1.123070</td>
      <td>-0.372262</td>
      <td>-0.340214</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.304163</td>
      <td>0.900263</td>
      <td>-1.663322</td>
      <td>0.633026</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.359713</td>
      <td>0.766208</td>
      <td>-0.460340</td>
      <td>0.746346</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.576092</td>
      <td>0.864615</td>
      <td>0.065375</td>
      <td>-1.200949</td>
    </tr>
  </tbody>
</table>
</div>



注意，如果使用了 `loc` 或者 `iloc`，**pandas** 会先对齐所有 `axes`。这不会修改 `df`，因为列对齐在赋值之前。


```python
df.loc[:, ['B', 'A']] = df[['A', 'B']]
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>-0.158166</td>
      <td>0.169225</td>
      <td>-0.166857</td>
      <td>-0.078189</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.631690</td>
      <td>0.584719</td>
      <td>0.001675</td>
      <td>0.263198</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-1.622012</td>
      <td>-0.234786</td>
      <td>-0.705652</td>
      <td>-0.171561</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-1.316517</td>
      <td>1.038103</td>
      <td>-0.135135</td>
      <td>-0.411320</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>0.290033</td>
      <td>1.123070</td>
      <td>-0.372262</td>
      <td>-0.340214</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.304163</td>
      <td>0.900263</td>
      <td>-1.663322</td>
      <td>0.633026</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.359713</td>
      <td>0.766208</td>
      <td>-0.460340</td>
      <td>0.746346</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>-0.576092</td>
      <td>0.864615</td>
      <td>0.065375</td>
      <td>-1.200949</td>
    </tr>
  </tbody>
</table>
</div>



可以强转成 `ndarray` 数组来实现这一操作：


```python
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.169225</td>
      <td>-0.158166</td>
      <td>-0.166857</td>
      <td>-0.078189</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.584719</td>
      <td>0.631690</td>
      <td>0.001675</td>
      <td>0.263198</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-0.234786</td>
      <td>-1.622012</td>
      <td>-0.705652</td>
      <td>-0.171561</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>1.038103</td>
      <td>-1.316517</td>
      <td>-0.135135</td>
      <td>-0.411320</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.123070</td>
      <td>0.290033</td>
      <td>-0.372262</td>
      <td>-0.340214</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>0.900263</td>
      <td>0.304163</td>
      <td>-1.663322</td>
      <td>0.633026</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>0.766208</td>
      <td>0.359713</td>
      <td>-0.460340</td>
      <td>0.746346</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.864615</td>
      <td>-0.576092</td>
      <td>0.065375</td>
      <td>-1.200949</td>
    </tr>
  </tbody>
</table>
</div>



### 切片

切片的规则和 **Python** 以及 **NumPy** 中的切片规则，一样。这里用 `[]` 运算符说明切片的语义。


```python
s = pd.Series(np.random.randn(7), index=list('abcdefg'))
s
```




    a   -0.381270
    b   -0.485434
    c   -0.298939
    d    0.508133
    e    0.961189
    f    0.107214
    g   -1.452212
    dtype: float64




```python
s[:5]
```




    a   -0.381270
    b   -0.485434
    c   -0.298939
    d    0.508133
    e    0.961189
    dtype: float64




```python
s[::2]
```




    a   -0.381270
    c   -0.298939
    e    0.961189
    g   -1.452212
    dtype: float64




```python
s[::-1]
```




    g   -1.452212
    f    0.107214
    e    0.961189
    d    0.508133
    c   -0.298939
    b   -0.485434
    a   -0.381270
    dtype: float64




```python
s[:3] = 0
s
```




    a    0.000000
    b    0.000000
    c    0.000000
    d    0.508133
    e    0.961189
    f    0.107214
    g   -1.452212
    dtype: float64




```python
df = pd.DataFrame(np.random.randn(3, 4), index=list('abc'), columns=list('ABCD'))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.871967</td>
      <td>1.381672</td>
      <td>0.395105</td>
      <td>-1.459083</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.466618</td>
      <td>1.626593</td>
      <td>-1.002821</td>
      <td>0.092995</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.384346</td>
      <td>0.020456</td>
      <td>-0.441192</td>
      <td>-0.476958</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[:2]
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.871967</td>
      <td>1.381672</td>
      <td>0.395105</td>
      <td>-1.459083</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.466618</td>
      <td>1.626593</td>
      <td>-1.002821</td>
      <td>0.092995</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[::-1]
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>0.384346</td>
      <td>0.020456</td>
      <td>-0.441192</td>
      <td>-0.476958</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.466618</td>
      <td>1.626593</td>
      <td>-1.002821</td>
      <td>0.092995</td>
    </tr>
    <tr>
      <th>a</th>
      <td>0.871967</td>
      <td>1.381672</td>
      <td>0.395105</td>
      <td>-1.459083</td>
    </tr>
  </tbody>
</table>
</div>



## 通过属性索引


```python
s = pd.Series([1, 2, 3], index=list('abc'))
s
```




    a    1
    b    2
    c    3
    dtype: int64




```python
s.b
```




    2




```python
df = pd.DataFrame(np.random.randn(3, 4), index=list('abc'), columns=list('ABCD'))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0.147620</td>
      <td>-1.336105</td>
      <td>0.945316</td>
      <td>0.501963</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1.220405</td>
      <td>0.697981</td>
      <td>-0.869925</td>
      <td>0.790545</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.935809</td>
      <td>0.584775</td>
      <td>1.316057</td>
      <td>0.138111</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.A
```




    a    0.147620
    b    1.220405
    c    0.935809
    Name: A, dtype: float64




```python
df.A = list(range(len(df.index)))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>-1.336105</td>
      <td>0.945316</td>
      <td>0.501963</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>0.697981</td>
      <td>-0.869925</td>
      <td>0.790545</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>0.584775</td>
      <td>1.316057</td>
      <td>0.138111</td>
    </tr>
  </tbody>
</table>
</div>



采用访问属性的方法必须确保该属性存在。如果要创建新的一列，仍然需要通过 `[]`。否则，会出现 `UserWanring` 的警告。


```python
df['E'] = list(range(len(df.index)))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>0</td>
      <td>-1.336105</td>
      <td>0.945316</td>
      <td>0.501963</td>
      <td>0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>0.697981</td>
      <td>-0.869925</td>
      <td>0.790545</td>
      <td>1</td>
    </tr>
    <tr>
      <th>c</th>
      <td>2</td>
      <td>0.584775</td>
      <td>1.316057</td>
      <td>0.138111</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## 通过标签索引

使用 `loc` 方法可以使用标签对行进行索引。


```python
s = pd.Series(np.random.randn(6), index=list('abcdef'))
s
```




    a    0.763607
    b   -0.538096
    c   -0.032027
    d    0.312734
    e    1.096504
    f   -0.857242
    dtype: float64




```python
s.loc['b']
```




    -0.5380958810076775



标签支持冒号表达式，进行切片运算。


```python
s.loc['c':]
```




    c   -0.032027
    d    0.312734
    e    1.096504
    f   -0.857242
    dtype: float64




```python
df = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.367401</td>
      <td>2.027401</td>
      <td>-0.379841</td>
      <td>-1.462746</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.032665</td>
      <td>0.143619</td>
      <td>-2.085444</td>
      <td>0.442935</td>
    </tr>
    <tr>
      <th>c</th>
      <td>-1.117230</td>
      <td>0.937448</td>
      <td>0.738852</td>
      <td>-0.411036</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.238427</td>
      <td>0.326619</td>
      <td>0.182713</td>
      <td>1.151853</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.454272</td>
      <td>0.844479</td>
      <td>-1.220454</td>
      <td>-1.453612</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.706529</td>
      <td>-0.733242</td>
      <td>0.400927</td>
      <td>-0.431352</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame 对象可以行列同时索引。


```python
df.loc[['a', 'b', 'd'], ['A', 'C']]
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
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.367401</td>
      <td>-0.379841</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.032665</td>
      <td>-2.085444</td>
    </tr>
    <tr>
      <th>d</th>
      <td>0.238427</td>
      <td>0.182713</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['d':, 'A':'C']
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
      <th>d</th>
      <td>0.238427</td>
      <td>0.326619</td>
      <td>0.182713</td>
    </tr>
    <tr>
      <th>e</th>
      <td>0.454272</td>
      <td>0.844479</td>
      <td>-1.220454</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.706529</td>
      <td>-0.733242</td>
      <td>0.400927</td>
    </tr>
  </tbody>
</table>
</div>



注意：下面的切片不是下标切片，而是标签切片。因此，`3:5` 表示标签 `3` 和 `5` 之间的所有标签。`3` 和 `5` 之间还有一个标签 `2`，因此返回结果为：


```python
s = pd.Series(list('abcdef'), index=[0, 3, 2, 5, 4, 2])
s.loc[3:5]
```




    3    b
    2    c
    5    d
    dtype: object



## 通过下标位置索引

使用 `iloc` 方法可以通过下标位置进行索引。


```python
s = pd.Series(np.random.randn(5), index=list(range(0, 10, 2)))
s
```




    0   -0.465348
    2   -0.507533
    4    0.600791
    6   -0.485520
    8    0.703295
    dtype: float64




```python
s.iloc[:3]
```




    0   -0.465348
    2   -0.507533
    4    0.600791
    dtype: float64




```python
s.iloc[-1]
```




    0.7032949052125851




```python
df = pd.DataFrame(np.random.randn(6, 4),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 8, 2)))
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
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.490701</td>
      <td>-0.549809</td>
      <td>0.504431</td>
      <td>-1.027572</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.790752</td>
      <td>0.687135</td>
      <td>0.674383</td>
      <td>-1.053664</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.168693</td>
      <td>-0.129001</td>
      <td>0.078535</td>
      <td>-0.770111</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.711808</td>
      <td>-0.269357</td>
      <td>1.663142</td>
      <td>-1.358983</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-0.405399</td>
      <td>-0.868119</td>
      <td>0.183488</td>
      <td>-1.307719</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2.091057</td>
      <td>0.426331</td>
      <td>0.120099</td>
      <td>0.599744</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame 对象可以行列同时索引。


```python
df.iloc[:3]
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
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.490701</td>
      <td>-0.549809</td>
      <td>0.504431</td>
      <td>-1.027572</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.790752</td>
      <td>0.687135</td>
      <td>0.674383</td>
      <td>-1.053664</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.168693</td>
      <td>-0.129001</td>
      <td>0.078535</td>
      <td>-0.770111</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:5, 2:4]
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
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0.674383</td>
      <td>-1.053664</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.078535</td>
      <td>-0.770111</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.663142</td>
      <td>-1.358983</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.183488</td>
      <td>-1.307719</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[[1, 3, 5], [1, 3]]
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
      <th>2</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>0.687135</td>
      <td>-1.053664</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.269357</td>
      <td>-1.358983</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.426331</td>
      <td>0.599744</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[1:3, :]
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
      <th>0</th>
      <th>2</th>
      <th>4</th>
      <th>6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>-1.790752</td>
      <td>0.687135</td>
      <td>0.674383</td>
      <td>-1.053664</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.168693</td>
      <td>-0.129001</td>
      <td>0.078535</td>
      <td>-0.770111</td>
    </tr>
  </tbody>
</table>
</div>



可以超出索引范围，但是可能会返回空 DataFrame。


```python
df.iloc[:, 4:]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
    </tr>
    <tr>
      <th>2</th>
    </tr>
    <tr>
      <th>4</th>
    </tr>
    <tr>
      <th>6</th>
    </tr>
    <tr>
      <th>8</th>
    </tr>
    <tr>
      <th>10</th>
    </tr>
  </tbody>
</table>
</div>



## 选择接受可调用对象

`[]`、`loc` 和 `iloc` 都接受可调用对象进行索引。


```python
df = pd.DataFrame(np.random.randn(6, 4),
                   index=list('abcdef'),
                   columns=list('ABCD'))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>-0.363806</td>
      <td>2.135196</td>
      <td>0.112095</td>
      <td>0.183855</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.964061</td>
      <td>1.549231</td>
      <td>0.162025</td>
      <td>1.408502</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.033714</td>
      <td>0.484294</td>
      <td>0.895077</td>
      <td>1.834204</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.632735</td>
      <td>0.628079</td>
      <td>1.497278</td>
      <td>1.194587</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-1.692414</td>
      <td>0.494285</td>
      <td>1.618099</td>
      <td>-1.882802</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.543841</td>
      <td>0.550801</td>
      <td>-1.429393</td>
      <td>-0.001107</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[lambda df: df['A'] > 0, :]
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>0.964061</td>
      <td>1.549231</td>
      <td>0.162025</td>
      <td>1.408502</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.033714</td>
      <td>0.484294</td>
      <td>0.895077</td>
      <td>1.834204</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[:, lambda df: ['A', 'B']]
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
      <th>a</th>
      <td>-0.363806</td>
      <td>2.135196</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.964061</td>
      <td>1.549231</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.033714</td>
      <td>0.484294</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.632735</td>
      <td>0.628079</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-1.692414</td>
      <td>0.494285</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.543841</td>
      <td>0.550801</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[:, lambda df: [0, 1]]
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
      <th>a</th>
      <td>-0.363806</td>
      <td>2.135196</td>
    </tr>
    <tr>
      <th>b</th>
      <td>0.964061</td>
      <td>1.549231</td>
    </tr>
    <tr>
      <th>c</th>
      <td>0.033714</td>
      <td>0.484294</td>
    </tr>
    <tr>
      <th>d</th>
      <td>-1.632735</td>
      <td>0.628079</td>
    </tr>
    <tr>
      <th>e</th>
      <td>-1.692414</td>
      <td>0.494285</td>
    </tr>
    <tr>
      <th>f</th>
      <td>-1.543841</td>
      <td>0.550801</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[lambda df: df.columns[0]]
```




    a   -0.363806
    b    0.964061
    c    0.033714
    d   -1.632735
    e   -1.692414
    f   -1.543841
    Name: A, dtype: float64




```python
df['A'].loc[lambda s: s > 0]
```




    b    0.964061
    c    0.033714
    Name: A, dtype: float64



## 快速访问

由于使用 `[]` 进行索引必须处理很多情况（单标签访问、切片、布尔索引等），因此它需要一些开销才能确定您的要求。如果您只想访问一个标量值，最快的方法是使用 `at` 和 `iat` 方法，它们在所有数据结构上都实现了。


```python
s = pd.Series(np.random.randint(0, 7, size=(7,)), index=list('abcdefg'))
s
```




    a    0
    b    6
    c    0
    d    6
    e    6
    f    1
    g    1
    dtype: int32




```python
s.iat[5]
```




    1




```python
s.at['a']
```




    0




```python
df = pd.DataFrame(np.random.randint(0, 7, size=(3, 4)), index=list('abc'), columns=list('ABCD'))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1</td>
      <td>5</td>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>b</th>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>c</th>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iat[0, 1]
```




    5




```python
df.at['b', 'A']
```




    1



## 布尔索引

Series 对象的布尔索引和 **Python** 以及 **NumPy** 类似。


```python
s = pd.Series(range(-3, 4))
s
```




    0   -3
    1   -2
    2   -1
    3    0
    4    1
    5    2
    6    3
    dtype: int64




```python
s[s > 0]
```




    4    1
    5    2
    6    3
    dtype: int64




```python
s[(s < -1) | (s > 0.5)]
```




    0   -3
    1   -2
    4    1
    5    2
    6    3
    dtype: int64




```python
s[~(s < 0)]
```




    3    0
    4    1
    5    2
    6    3
    dtype: int64




```python
df = pd.DataFrame(np.random.randn(7, 4),
                  index=pd.date_range('2022/02/22', periods=7),
                  columns=list('ABCD'))
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-02-22</th>
      <td>-1.645831</td>
      <td>-0.603577</td>
      <td>0.855909</td>
      <td>-0.172192</td>
    </tr>
    <tr>
      <th>2022-02-23</th>
      <td>-0.006510</td>
      <td>-0.708135</td>
      <td>-0.788163</td>
      <td>-2.029753</td>
    </tr>
    <tr>
      <th>2022-02-24</th>
      <td>-1.034041</td>
      <td>0.977184</td>
      <td>-0.176987</td>
      <td>-0.066881</td>
    </tr>
    <tr>
      <th>2022-02-25</th>
      <td>0.713977</td>
      <td>2.029726</td>
      <td>-0.441814</td>
      <td>0.105782</td>
    </tr>
    <tr>
      <th>2022-02-26</th>
      <td>-0.038251</td>
      <td>-1.624340</td>
      <td>-0.882659</td>
      <td>0.655924</td>
    </tr>
    <tr>
      <th>2022-02-27</th>
      <td>1.122102</td>
      <td>-0.019443</td>
      <td>1.120410</td>
      <td>-0.599446</td>
    </tr>
    <tr>
      <th>2022-02-28</th>
      <td>1.829295</td>
      <td>0.039461</td>
      <td>-0.468706</td>
      <td>1.038191</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[df['A'] > 0]
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-02-25</th>
      <td>0.713977</td>
      <td>2.029726</td>
      <td>-0.441814</td>
      <td>0.105782</td>
    </tr>
    <tr>
      <th>2022-02-27</th>
      <td>1.122102</td>
      <td>-0.019443</td>
      <td>1.120410</td>
      <td>-0.599446</td>
    </tr>
    <tr>
      <th>2022-02-28</th>
      <td>1.829295</td>
      <td>0.039461</td>
      <td>-0.468706</td>
      <td>1.038191</td>
    </tr>
  </tbody>
</table>
</div>



### 高级布尔函数

`isin(values)` 用于判断元素是否包含在 `values` 中，适用于 `Series`，`DataFrame` 和 `Index` 对象。


```python
df = pd.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
                  index=['falcon', 'dog'])
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
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



`isin` 函数可以接受 list、dict、Seires 等可迭代对象作为参数。


```python
df.isin([0, 2])
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
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



如果传入的是 dict，则可以分别设置每一列的判断规则。如若不设置，默认得到 False。


```python
df.isin({'num_wings': [0, 3]})
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
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



如果传入的是 Series 或者 DataFrame 对象，那么必须确保每行每列匹配。


```python
other = pd.DataFrame({'num_legs': [8, 3], 'num_wings': [0, 2]},
                     index=['spider', 'falcon'])
df.isin(other)
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
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



查询 `num_wings` 列中值为 2 或 4 的行。


```python
df[df["num_wings"].isin([2, 4])]
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
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



过滤并保留 `num_wings` 列中值为 4 或 8 的行。


```python
df = df[df["num_legs"].isin([4, 8])]
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
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


