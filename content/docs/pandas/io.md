---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "输入输出"
linktitle: "输入输出"
date: 2022-02-19T11:19:54+08:00
type: docs
summary: ""
weight: 70
---

<!--more-->

```python
import pandas as pd
import numpy as np

from io import StringIO
```

## CSV

### 数据交互


```python
data = "col1,col2,col3\na,b,1\na,b,2\nc,d,3"
pd.read_csv(StringIO(data))
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>d</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



可以仅指定部分列：


```python
pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ["COL1", "COL3"])
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
      <th>col1</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



也可以仅指定部分行：


```python
pd.read_csv(StringIO(data), skiprows=lambda x: x % 2 != 0)
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



可以使用 `names` 参数指定列名。如果希望替换原字符流第一行，则设置 `header=0`。


```python
data = "a,b,c\n1,2,3\n4,5,6\n7,8,9"
pd.read_csv(StringIO(data), names=["foo", "bar", "baz"], header=0)
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
      <th>foo</th>
      <th>bar</th>
      <th>baz</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



如果第一行也是数据，列名需要手动添加，则设置 `header=None`。


```python
pd.read_csv(StringIO(data), names=["foo", "bar", "baz"], header=None)
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
      <th>foo</th>
      <th>bar</th>
      <th>baz</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>b</td>
      <td>c</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



还可以实现跳过前面若干行的功能，例如跳过第一行：


```python
data = "skip this skip it\na,b,c\n1,2,3\n4,5,6\n7,8,9"
pd.read_csv(StringIO(data), header=1)
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
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



使用 `dtype='category'`，生成的类别将始终被解析为字符串。


```python
data = "col1,col2,col3\na,b,1\na,b,2\nc,d,3"
df = pd.read_csv(StringIO(data), dtype="category")
df.dtypes
```




    col1    category
    col2    category
    col3    category
    dtype: object



使用参数 `comment=#` 来忽略以 `#` 开头的注释。


```python
data = "\na,b,c\n  \n# commented line\n1,2,3\n\n4,5,6"
pd.read_csv(StringIO(data), comment="#")
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
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



使用参数 `skip_blank_lines` 来指定是否跳过空行，默认值为 `True`。


```python
data = "a,b,c\n\n1,2,3\n\n\n4,5,6"
pd.read_csv(StringIO(data), skip_blank_lines=False)
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
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>5.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>



### 文件读写


```python
df = pd.DataFrame(np.random.randint(0, 10, size=(3, 4)),
                  index=pd.date_range('2022/2/22', periods=3),
                  columns=list('ABCD'))
df.to_csv('dist/foo.csv', encoding='utf-8')
```

参数 `index_col=0` 指定 `csv` 文件的第一列为 `index`。


```python
pd.read_csv('src/foo.csv', index_col=0)
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
      <td>9</td>
      <td>4</td>
      <td>9</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2022-02-23</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2022-02-24</th>
      <td>5</td>
      <td>9</td>
      <td>8</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



## Excel

使用 **pandas** 读写 Excel 文件需要安装 `openpyxl` 包。


```python
df = pd.DataFrame(np.random.randint(0, 10, size=(3, 4)),
                  index=pd.date_range('2022/2/22', periods=3),
                  columns=list('ABCD'))
df.to_excel('dist/foo.xlsx', sheet_name='Sheet1')
```


```python
pd.read_excel('src/foo.xlsx', sheet_name='Sheet1', index_col=0, na_values=['NA'])
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
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2022-02-23</th>
      <td>0</td>
      <td>6</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2022-02-24</th>
      <td>3</td>
      <td>2</td>
      <td>6</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



如果要读取一个 Excel 文件的多个 Sheet，使用 `ExcelFile` 对象。


```python
data = {}

with pd.ExcelFile("src/foo.xlsx") as xlsx:
    data["Sheet1"] = pd.read_excel(xlsx, "Sheet1", index_col=0, na_values=['NA'])
    data["Sheet2"] = pd.read_excel(xlsx, "Sheet2", index_col=0, na_values=['NA'])

data
```




    {'Sheet1':             A  B  C  D
     2022-02-22  2  2  8  1
     2022-02-23  0  6  4  2
     2022-02-24  3  2  6  6,
     'Sheet2':             A  B  C  D
     2022-02-22  1  2  4  3
     2022-02-23  3  2  1  2
     2022-02-24  3  1  4  6}


