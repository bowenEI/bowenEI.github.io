---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "合并与连接"
linktitle: "合并与连接"
date: 2022-02-19T11:18:56+08:00
type: docs
summary: ""
weight: 50
---

<!--more-->

```python
import pandas as pd
```

## concat: 合并多个 DataFrame 和 Series

### 垂直合并


```python
left = pd.DataFrame({'Name': ['Sam', 'Emma'], 'Age': [14, 15]})
left
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
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
right = pd.DataFrame({'Name': ['Karen', 'Rahul'], 'Age': [10, 13]})
right
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
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Karen</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rahul</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>



垂直合并即按列合并，一般需要 DataFrame 的 column 完全一致。


```python
pd.concat([left, right])
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
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Karen</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Rahul</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>



不过，上面的结果仍然保留了这些 DataFrame 原来的索引。我们可以重置索引：


```python
pd.concat([left, right]).reset_index(drop=True)
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
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Karen</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rahul</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>



### 水平合并


```python
left = pd.DataFrame({'Name': ['Sam', 'Emma'], 'Age': [14, 15]})
left
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
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
right = pd.DataFrame({'Math': ['B', 'A+'], 'Science': ['A', 'B+']})
right
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
      <th>Math</th>
      <th>Science</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A+</td>
      <td>B+</td>
    </tr>
  </tbody>
</table>
</div>



设置 `axis=1` 即可实现水平合并，即按行合并，一般要求 DataFrame 的 index 完全一致。


```python
pd.concat([left, right], axis=1)
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
      <th>Age</th>
      <th>Math</th>
      <th>Science</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14</td>
      <td>B</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15</td>
      <td>A+</td>
      <td>B+</td>
    </tr>
  </tbody>
</table>
</div>



### 设置合并模式

如果 index 或者 column 不一致，则可以设置连接 `join` 的方式。


- `outer`：类似于关系代数的外连接运算，没有的内容补 NaN 值。该选项为默认值。
- `inner`：类似于关系代数的自然连接运算，先求笛卡尔积中对应相等的元组，再去掉其中重复的属性值。

注：与关系代数不同的是，**pandas** 对 DataFrame 的连接可以在 index 和 column 上都可以进行。


```python
left = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
left
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
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    },
    index=[2, 3, 6, 7],
)
right
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
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B6</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B7</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([left, right], axis=1, join='outer')
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
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>B6</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>B7</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([left, right], axis=1, join='inner')
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
      <th>B</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>B2</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>B3</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([left, right], axis=0, join='outer')
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
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>B2</td>
      <td>NaN</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>B3</td>
      <td>NaN</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>B6</td>
      <td>NaN</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>B7</td>
      <td>NaN</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([left, right], axis=0, join='inner')
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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>B2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B6</td>
      <td>D6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>B7</td>
      <td>D7</td>
    </tr>
  </tbody>
</table>
</div>



可以设置忽略 index，index 将按照顺序递增。这样就和关系代数中的连接运算完全一致了。


```python
pd.concat([left, right], ignore_index=True)
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
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>B2</td>
      <td>NaN</td>
      <td>D2</td>
      <td>F2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>B3</td>
      <td>NaN</td>
      <td>D3</td>
      <td>F3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>B6</td>
      <td>NaN</td>
      <td>D6</td>
      <td>F6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>B7</td>
      <td>NaN</td>
      <td>D7</td>
      <td>F7</td>
    </tr>
  </tbody>
</table>
</div>



### DataFrame 和 Series 可以直接合并


```python
s = pd.Series(["X0", "X1", "X2", "X3"], name="X")
s
```




    0    X0
    1    X1
    2    X2
    3    X3
    Name: X, dtype: object




```python
df = pd.DataFrame({'Name': ['Sam', 'Emma'], 'Age': [14, 15]})
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
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df, s], axis=1)
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
      <th>Age</th>
      <th>X</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sam</td>
      <td>14.0</td>
      <td>X0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Emma</td>
      <td>15.0</td>
      <td>X1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>X2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>X3</td>
    </tr>
  </tbody>
</table>
</div>



## merge: 功能更强大的数据库连接操作


```python
left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
left
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
      <th>key</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
right
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
      <th>key</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, on='key')
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
      <th>key</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K2</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K3</td>
      <td>A3</td>
      <td>B3</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



### 连接方式

`merge` 可以实现关系代数当中的除自然连接和外连接更强大的连接操作。因此，它的 `how` 参数支持如下五种运算：

- `outer`：外连接
- `inner`：自然连接
- `left`：左连接
- `right`：右连接
- `cross`：笛卡尔积

这种运算要求左表和右表有交叉点 `intersection` 存在，因此连接方式默认值为 `inner`。


```python
left = pd.DataFrame(
    {
        "key1": ["K0", "K0", "K1", "K2"],
        "key2": ["K0", "K1", "K0", "K1"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
left
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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
    </tr>
  </tbody>
</table>
</div>




```python
right = pd.DataFrame(
    {
        "key1": ["K0", "K1", "K1", "K2"],
        "key2": ["K0", "K0", "K0", "K0"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
right
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
      <th>key1</th>
      <th>key2</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K0</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



这个例子是由两个字段组成主码的表的连接操作。


```python
pd.merge(left, right, on=["key1", "key2"])
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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>



#### 自然连接


```python
pd.merge(left, right, how="inner", on=["key1", "key2"])
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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>



#### 外连接


```python
pd.merge(left, right, how="outer", on=["key1", "key2"])
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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K2</td>
      <td>K0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### 左连接


```python
pd.merge(left, right, how="left", on=["key1", "key2"])
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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### 右连接


```python
pd.merge(left, right, how="right", on=["key1", "key2"])
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
      <th>key1</th>
      <th>key2</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K2</td>
      <td>K0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



#### 笛卡尔积


```python
pd.merge(left, right, how="cross")
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
      <th>key1_x</th>
      <th>key2_x</th>
      <th>A</th>
      <th>B</th>
      <th>key1_y</th>
      <th>key2_y</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>K0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>K1</td>
      <td>K0</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>K1</td>
      <td>K0</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>K0</td>
      <td>K0</td>
      <td>A0</td>
      <td>B0</td>
      <td>K2</td>
      <td>K0</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>K0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>K1</td>
      <td>K0</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>K1</td>
      <td>K0</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>K0</td>
      <td>K1</td>
      <td>A1</td>
      <td>B1</td>
      <td>K2</td>
      <td>K0</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>K0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>K1</td>
      <td>K0</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>K1</td>
      <td>K0</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>K1</td>
      <td>K0</td>
      <td>A2</td>
      <td>B2</td>
      <td>K2</td>
      <td>K0</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>K0</td>
      <td>K0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>K1</td>
      <td>K0</td>
      <td>C1</td>
      <td>D1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>K1</td>
      <td>K0</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>K2</td>
      <td>K1</td>
      <td>A3</td>
      <td>B3</td>
      <td>K2</td>
      <td>K0</td>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>



## join: DataFrame 对象的强大连接操作


```python
left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)
left
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
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
    </tr>
  </tbody>
</table>
</div>




```python
right = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)
right
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
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>C2</td>
      <td>D2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>C3</td>
      <td>D3</td>
    </tr>
  </tbody>
</table>
</div>




```python
left.join(right)
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
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K1</th>
      <td>A1</td>
      <td>B1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>




```python
right.join(left)
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
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>K0</th>
      <td>C0</td>
      <td>D0</td>
      <td>A0</td>
      <td>B0</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>C2</td>
      <td>D2</td>
      <td>A2</td>
      <td>B2</td>
    </tr>
    <tr>
      <th>K3</th>
      <td>C3</td>
      <td>D3</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame 的 `join` 默认值为 `left`，可以设置为除笛卡尔积外的连接方式。


```python
left.join(right, how='inner')
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
      <th>K0</th>
      <td>A0</td>
      <td>B0</td>
      <td>C0</td>
      <td>D0</td>
    </tr>
    <tr>
      <th>K2</th>
      <td>A2</td>
      <td>B2</td>
      <td>C2</td>
      <td>D2</td>
    </tr>
  </tbody>
</table>
</div>


