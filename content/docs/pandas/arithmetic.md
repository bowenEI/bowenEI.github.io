---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "基本运算"
linktitle: "基本运算"
date: 2022-03-04T11:07:16+08:00
type: docs
summary: ""
weight: 35
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

## 算术运算


```python
df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
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
      <td>0.760609</td>
      <td>0.613241</td>
      <td>0.364961</td>
      <td>0.410891</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.595899</td>
      <td>-0.036977</td>
      <td>1.638757</td>
      <td>0.324315</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.449550</td>
      <td>1.454056</td>
      <td>-0.350593</td>
      <td>-1.610116</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.504186</td>
      <td>-1.939660</td>
      <td>-0.858069</td>
      <td>-0.092820</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.460082</td>
      <td>1.774454</td>
      <td>2.345259</td>
      <td>0.466701</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.773129</td>
      <td>-0.156779</td>
      <td>1.424565</td>
      <td>-1.076731</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.861531</td>
      <td>-0.962290</td>
      <td>2.189390</td>
      <td>-0.174458</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.335252</td>
      <td>-0.239888</td>
      <td>-0.716997</td>
      <td>-0.279536</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.123587</td>
      <td>-0.166000</td>
      <td>-0.722529</td>
      <td>0.148577</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.438719</td>
      <td>-0.208563</td>
      <td>-0.774170</td>
      <td>2.349832</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.989388</td>
      <td>-0.268563</td>
      <td>1.160158</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.293817</td>
      <td>2.287877</td>
      <td>0.461996</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.359939</td>
      <td>-0.985352</td>
      <td>0.628079</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.094576</td>
      <td>-0.109829</td>
      <td>-0.526178</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.462213</td>
      <td>0.654518</td>
      <td>1.245316</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.222436</td>
      <td>-1.475495</td>
      <td>0.904898</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.060508</td>
      <td>0.013139</td>
      <td>1.111483</td>
    </tr>
  </tbody>
</table>
</div>




```python
df * 5 + 2
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
      <td>6.946938</td>
      <td>0.657185</td>
      <td>7.800790</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.530917</td>
      <td>13.439387</td>
      <td>4.309981</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.799693</td>
      <td>-2.926762</td>
      <td>5.140393</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.527120</td>
      <td>1.450855</td>
      <td>-0.630888</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.311063</td>
      <td>5.272590</td>
      <td>8.226580</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.887822</td>
      <td>-5.377473</td>
      <td>6.524490</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2.302542</td>
      <td>2.065696</td>
      <td>7.557416</td>
    </tr>
  </tbody>
</table>
</div>




```python
1 / df
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
      <td>1.010726</td>
      <td>-3.723522</td>
      <td>0.861952</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-3.403484</td>
      <td>0.437086</td>
      <td>2.164520</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.778252</td>
      <td>-1.014865</td>
      <td>1.592158</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-10.573505</td>
      <td>-9.105061</td>
      <td>-1.900499</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.163507</td>
      <td>1.527842</td>
      <td>0.803009</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-4.495684</td>
      <td>-0.677739</td>
      <td>1.105097</td>
    </tr>
    <tr>
      <th>6</th>
      <td>16.526648</td>
      <td>76.107908</td>
      <td>0.899699</td>
    </tr>
  </tbody>
</table>
</div>




```python
df ** 4
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
      <td>0.958222</td>
      <td>5.202168e-03</td>
      <td>1.811626</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.007453</td>
      <td>2.739876e+01</td>
      <td>0.045557</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.016785</td>
      <td>9.426843e-01</td>
      <td>0.155617</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.000080</td>
      <td>1.455019e-04</td>
      <td>0.076653</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.045642</td>
      <td>1.835213e-01</td>
      <td>2.405018</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.002448</td>
      <td>4.739696e+00</td>
      <td>0.670500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.000013</td>
      <td>2.980443e-08</td>
      <td>1.526201</td>
    </tr>
  </tbody>
</table>
</div>



## 布尔运算


```python
df = pd.DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]}, dtype=bool)
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame({"a": [0, 1, 1], "b": [1, 1, 0]}, dtype=bool)
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df & df
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
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df | df
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
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df ^ df
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
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
-df
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
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


