---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "分类汇总"
linktitle: "分类汇总"
date: 2022-02-19T11:19:27+08:00
type: docs
summary: ""
weight: 60
---

<!--more-->

```python
import pandas as pd
import numpy as np
```

分类汇总 `group by` 指的是如下的一个或多个步骤的数据分组：

- **Splitting**: 根据某些标准将数据分成若干组。
- **Applying**: 将一个函数独立应用于每个组。
- **Combining**: 将结果合并到数据结构中。

其中，拆分步骤最简单。事实上，在许多情况下，我们可能希望将数据集分成若干组，并对这些组进行处理。

在应用步骤中，我们可能希望执行以下操作之一：

- **Aggregation**: 计算每组的汇总统计数据。例如计算每组的和 `sum` 以及平均值 `means`，或者数每组记录的个数。
- **Transformation**: 执行一些特定于组的计算，并返回一个相似的索引对象。例如获得每组排序后的第一个数据。
- **Filtration**: 根据评估为真或假的分组计算，丢弃一些分组。例如丢弃属于只有少数成员的组的数据，或者根据组和或平均值过滤数据。

## 分组

pandas 对象可以在其任意轴上拆分。分组的抽象定义是提供标签到组名的映射。分组需要创建 `GroupBy` 对象。


```python
df = pd.DataFrame(
    [
        ("bird", "Falconiformes", 389.0),
        ("bird", "Psittaciformes", 24.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),
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

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>class</th>
      <th>order</th>
      <th>max_speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>bird</td>
      <td>Falconiformes</td>
      <td>389.0</td>
    </tr>
    <tr>
      <th>parrot</th>
      <td>bird</td>
      <td>Psittaciformes</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>lion</th>
      <td>mammal</td>
      <td>Carnivora</td>
      <td>80.2</td>
    </tr>
    <tr>
      <th>monkey</th>
      <td>mammal</td>
      <td>Primates</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>leopard</th>
      <td>mammal</td>
      <td>Carnivora</td>
      <td>58.0</td>
    </tr>
  </tbody>
</table>
</div>



按行分组。


```python
df.groupby('class')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001BC34299A10>



按多个字段分组。


```python
df.groupby(['class', 'order'])
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001BC3427E710>



通常一张数据表每一行表示一条记录，每一列表示一个字段。因而分类汇总是针对字段，对每条记录（按行）进行分组。如果确实有按列进行分组的需求，将 DataFrame 对象转置即可。

## 应用与合并

### 汇总


```python
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
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
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>0.106162</td>
      <td>-0.093786</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>one</td>
      <td>-0.179389</td>
      <td>2.213905</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>-0.190954</td>
      <td>0.082038</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>three</td>
      <td>0.312979</td>
      <td>1.034273</td>
    </tr>
    <tr>
      <th>4</th>
      <td>foo</td>
      <td>two</td>
      <td>1.052136</td>
      <td>-0.130627</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>two</td>
      <td>-1.220164</td>
      <td>1.215908</td>
    </tr>
    <tr>
      <th>6</th>
      <td>foo</td>
      <td>one</td>
      <td>-0.926031</td>
      <td>-1.477368</td>
    </tr>
    <tr>
      <th>7</th>
      <td>foo</td>
      <td>three</td>
      <td>0.157087</td>
      <td>1.622384</td>
    </tr>
  </tbody>
</table>
</div>



`GroupBy` 对象后索引 column 表示需要汇总的属性，会返回一个新的 `GroupBy` 对象。


```python
grouped = df.groupby('A')[['C', 'D']]
```

#### 求和


```python
grouped.sum()
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
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-1.086574</td>
      <td>4.464086</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.198399</td>
      <td>0.002641</td>
    </tr>
  </tbody>
</table>
</div>



#### 平均值


```python
grouped.mean()
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
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-0.362191</td>
      <td>1.488029</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.039680</td>
      <td>0.000528</td>
    </tr>
  </tbody>
</table>
</div>



#### 中位数


```python
grouped.median()
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
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-0.179389</td>
      <td>1.215908</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.106162</td>
      <td>-0.093786</td>
    </tr>
  </tbody>
</table>
</div>



#### 最小值


```python
grouped.min()
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
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-1.220164</td>
      <td>1.034273</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-0.926031</td>
      <td>-1.477368</td>
    </tr>
  </tbody>
</table>
</div>



#### 最大值


```python
grouped.max()
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
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>0.312979</td>
      <td>2.213905</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>1.052136</td>
      <td>1.622384</td>
    </tr>
  </tbody>
</table>
</div>



#### 标准差


```python
grouped.std()
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
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>0.782748</td>
      <td>0.635154</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.712226</td>
      <td>1.100833</td>
    </tr>
  </tbody>
</table>
</div>



可以使用 `agg` 来使用任何可以进行汇总和统计的函数，包括用户自定义的函数。


```python
grouped.agg(['sum', 'mean'])
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

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">C</th>
      <th colspan="2" halign="left">D</th>
    </tr>
    <tr>
      <th></th>
      <th>sum</th>
      <th>mean</th>
      <th>sum</th>
      <th>mean</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-1.086574</td>
      <td>-0.362191</td>
      <td>4.464086</td>
      <td>1.488029</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.198399</td>
      <td>0.039680</td>
      <td>0.002641</td>
      <td>0.000528</td>
    </tr>
  </tbody>
</table>
</div>



### 次序


```python
df = pd.DataFrame({
    'Name': ['Jim', 'Jim', 'Jim', 'Pam', 'Pam'],
    'Attempt': ['First', 'Second', 'Third', 'First', 'Second'],
    'GRE Score': [298, 321, 314, 318, 330]
})
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
      <th>Name</th>
      <th>Attempt</th>
      <th>GRE Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jim</td>
      <td>First</td>
      <td>298</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jim</td>
      <td>Second</td>
      <td>321</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jim</td>
      <td>Third</td>
      <td>314</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pam</td>
      <td>First</td>
      <td>318</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pam</td>
      <td>Second</td>
      <td>330</td>
    </tr>
  </tbody>
</table>
</div>



返回每个人最后一次 GRE 考试成绩：


```python
df.groupby('Name')['GRE Score'].last()
```




    Name
    Jim    314
    Pam    330
    Name: GRE Score, dtype: int64



返回每个人第一次 GRE 考试成绩：


```python
df.groupby('Name')['GRE Score'].first()
```




    Name
    Jim    298
    Pam    318
    Name: GRE Score, dtype: int64



使用 `nth` 可以返回第任意次 GRE 考试成绩：


```python
df.groupby('Name')['GRE Score'].nth(1)
```




    1    321
    4    330
    Name: GRE Score, dtype: int64



### 排序

给每次 GRE 考试都加上名次。


```python
df['Rank'] = df.groupby('Name')['GRE Score'].rank(ascending=False).astype(int)
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
      <th>Name</th>
      <th>Attempt</th>
      <th>GRE Score</th>
      <th>Rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jim</td>
      <td>First</td>
      <td>298</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jim</td>
      <td>Second</td>
      <td>321</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jim</td>
      <td>Third</td>
      <td>314</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pam</td>
      <td>First</td>
      <td>318</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pam</td>
      <td>Second</td>
      <td>330</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



如要给每组数据都排序，建议先对原 DataFrame 对象排序，再分组。


```python
df.sort_values('GRE Score', ascending=False).groupby('Name')['GRE Score'].first()
```




    Name
    Jim    321
    Pam    330
    Name: GRE Score, dtype: int64


