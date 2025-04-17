---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "数据对齐"
linktitle: "数据对齐"
date: 2022-02-19T11:17:40+08:00
type: docs
summary: ""
weight: 40
---

<!--more-->


```python
import pandas as pd
import numpy as np
```

## 广播机制

DataFrame 对象之间的数据对齐在列和索引（行标签）上自动对齐。同样，结果对象将得到列和行标签的并集。


```python
df1 = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
df1
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
      <td>-0.205518</td>
      <td>-1.079244</td>
      <td>0.466754</td>
      <td>0.697197</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.373488</td>
      <td>-0.704131</td>
      <td>-0.562608</td>
      <td>-0.747020</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.727782</td>
      <td>1.176981</td>
      <td>1.748998</td>
      <td>-2.381428</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.693188</td>
      <td>-0.236861</td>
      <td>-0.045300</td>
      <td>1.116772</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.679781</td>
      <td>-0.113023</td>
      <td>-0.237897</td>
      <td>0.991700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.301815</td>
      <td>-0.736582</td>
      <td>-0.327876</td>
      <td>1.240366</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.362792</td>
      <td>0.409796</td>
      <td>-0.559092</td>
      <td>1.486711</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.158763</td>
      <td>2.898433</td>
      <td>-1.066979</td>
      <td>1.109399</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.801811</td>
      <td>-0.150998</td>
      <td>0.256121</td>
      <td>0.626933</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.248901</td>
      <td>-0.846965</td>
      <td>0.728085</td>
      <td>-0.302709</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])
df2
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
      <td>0.656296</td>
      <td>0.948401</td>
      <td>1.203846</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.576805</td>
      <td>2.193866</td>
      <td>-1.295344</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.107251</td>
      <td>-1.394675</td>
      <td>1.322735</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.278274</td>
      <td>-0.398505</td>
      <td>-0.894721</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.798450</td>
      <td>-0.817746</td>
      <td>1.933429</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.856174</td>
      <td>0.212137</td>
      <td>-0.323455</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.148207</td>
      <td>2.293063</td>
      <td>0.164304</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 + df2
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
      <td>0.450778</td>
      <td>-0.130843</td>
      <td>1.670600</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.950293</td>
      <td>1.489735</td>
      <td>-1.857952</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.835033</td>
      <td>-0.217694</td>
      <td>3.071733</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.971461</td>
      <td>-0.635366</td>
      <td>-0.940020</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.478231</td>
      <td>-0.930769</td>
      <td>1.695532</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.554358</td>
      <td>-0.524445</td>
      <td>-0.651331</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.510998</td>
      <td>2.702860</td>
      <td>-0.394789</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



在 DataFrame 和 Series 之间执行操作时，默认行为是对齐 DataFrame 列上的 Series 索引，从而按行广播。例如：


```python
df1 - df1.iloc[0]
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
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.579007</td>
      <td>0.375113</td>
      <td>-1.029362</td>
      <td>-1.444217</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.933301</td>
      <td>2.256226</td>
      <td>1.282244</td>
      <td>-3.078625</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.898706</td>
      <td>0.842383</td>
      <td>-0.512054</td>
      <td>0.419576</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.885300</td>
      <td>0.966221</td>
      <td>-0.704651</td>
      <td>0.294503</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.507334</td>
      <td>0.342662</td>
      <td>-0.794630</td>
      <td>0.543169</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.157273</td>
      <td>1.489041</td>
      <td>-1.025846</td>
      <td>0.789514</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.364281</td>
      <td>3.977677</td>
      <td>-1.533733</td>
      <td>0.412202</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2.007330</td>
      <td>0.928246</td>
      <td>-0.210632</td>
      <td>-0.070263</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.454420</td>
      <td>0.232279</td>
      <td>0.261331</td>
      <td>-0.999906</td>
    </tr>
  </tbody>
</table>
</div>


