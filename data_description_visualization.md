# Automobile mile per gallon prediction

Predict automobile mile per gallon based on given features

## Dataset description

### Source

[Auto-mpg](https://archive.ics.uci.edu/dataset/9/auto+mpg)

### Samples

<table border="1">
  <thead>
    <tr>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model year</th>
      <th>origin</th>
      <th>car name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>18.0000</td>
      <td>8</td>
      <td>307.0000</td>
      <td>130</td>
      <td>3504</td>
      <td>12.0000</td>
      <td>70</td>
      <td>USA</td>
      <td>chevrolet chevelle malibu</td>
    </tr>
    <tr>
      <td>15.0000</td>
      <td>8</td>
      <td>350.0000</td>
      <td>165</td>
      <td>3693</td>
      <td>11.5000</td>
      <td>70</td>
      <td>USA</td>
      <td>buick skylark 320</td>
    </tr>
    <tr>
      <td>18.0000</td>
      <td>8</td>
      <td>318.0000</td>
      <td>150</td>
      <td>3436</td>
      <td>11.0000</td>
      <td>70</td>
      <td>USA</td>
      <td>plymouth satellite</td>
    </tr>
    <tr>
      <td>16.0000</td>
      <td>8</td>
      <td>304.0000</td>
      <td>150</td>
      <td>3433</td>
      <td>12.0000</td>
      <td>70</td>
      <td>USA</td>
      <td>amc rebel sst</td>
    </tr>
    <tr>
      <td>17.0000</td>
      <td>8</td>
      <td>302.0000</td>
      <td>140</td>
      <td>3449</td>
      <td>10.5000</td>
      <td>70</td>
      <td>USA</td>
      <td>ford torino</td>
    </tr>
    <!-- ... (add other rows as needed) ... -->
    <tr>
      <td>27.0000</td>
      <td>4</td>
      <td>140.0000</td>
      <td>86</td>
      <td>2790</td>
      <td>15.6000</td>
      <td>82</td>
      <td>USA</td>
      <td>ford mustang gl</td>
    </tr>
    <tr>
      <td>44.0000</td>
      <td>4</td>
      <td>97.0000</td>
      <td>52</td>
      <td>2130</td>
      <td>24.6000</td>
      <td>82</td>
      <td>Europe</td>
      <td>vw pickup</td>
    </tr>
    <tr>
      <td>32.0000</td>
      <td>4</td>
      <td>135.0000</td>
      <td>84</td>
      <td>2295</td>
      <td>11.6000</td>
      <td>82</td>
      <td>USA</td>
      <td>dodge rampage</td>
    </tr>
    <tr>
      <td>28.0000</td>
      <td>4</td>
      <td>120.0000</td>
      <td>79</td>
      <td>2625</td>
      <td>18.6000</td>
      <td>82</td>
      <td>USA</td>
      <td>ford ranger</td>
    </tr>
    <tr>
      <td>31.0000</td>
      <td>4</td>
      <td>119.0000</td>
      <td>82</td>
      <td>2720</td>
      <td>19.4000</td>
      <td>82</td>
      <td>USA</td>
      <td>chevy s-10</td>
    </tr>
  </tbody>
</table>

> **398 rows × 9 columns**

### Variable information

<table>
  <tr>
    <th>Variable Name</th>
    <th>Role</th>
    <th>Type</th>
    <th>Demographic</th>
    <th>Description</th>
    <th>Units</th>
    <th>Missing Values</th>
  </tr>
  <tr>
    <td>displacement</td>
    <td>Feature</td>
    <td>Continuous</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>mpg</td>
    <td>Target</td>
    <td>Continuous</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>cylinders</td>
    <td>Feature</td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>horsepower</td>
    <td>Feature</td>
    <td>Continuous</td>
    <td></td>
    <td></td>
    <td></td>
    <td>yes</td>
  </tr>
  <tr>
    <td>weight</td>
    <td>Feature</td>
    <td>Continuous</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>acceleration</td>
    <td>Feature</td>
    <td>Continuous</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>model_year</td>
    <td>Feature</td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>origin</td>
    <td>Feature</td>
    <td>Integer</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
  <tr>
    <td>car_name</td>
    <td>ID</td>
    <td>Categorical</td>
    <td></td>
    <td></td>
    <td></td>
    <td>no</td>
  </tr>
</table>

## Exploratory data analysis 

### Label mapping of origin 

<table border="1">
  <tr>
    <th>#</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>1</td>
    <td>USA</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Europe</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Japan</td>
  </tr>
</table>

### Checking for duplicates

**Across all features**

0 duplicates

**Across car name, origin, and model year (the same car)**

4 duplicates

<table border="1">
  <thead>
    <tr>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model year</th>
      <th>origin</th>
      <th>car name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>168</td>
      <td>4</td>
      <td>140.0000</td>
      <td>83</td>
      <td>2639</td>
      <td>17.0000</td>
      <td>75</td>
      <td>USA</td>
      <td>ford pinto</td>
    </tr>
    <tr>
      <td>174</td>
      <td>6</td>
      <td>171.0000</td>
      <td>97</td>
      <td>2984</td>
      <td>14.5000</td>
      <td>75</td>
      <td>USA</td>
      <td>ford pinto</td>
    </tr>
    <tr>
      <td>338</td>
      <td>4</td>
      <td>135.0000</td>
      <td>84</td>
      <td>2490</td>
      <td>15.7000</td>
      <td>81</td>
      <td>USA</td>
      <td>plymouth reliant</td>
    </tr>
    <tr>
      <td>342</td>
      <td>4</td>
      <td>135.0000</td>
      <td>84</td>
      <td>2385</td>
      <td>12.9000</td>
      <td>81</td>
      <td>USA</td>
      <td>plymouth reliant</td>
    </tr>
  </tbody>
</table>

> There is two samples for each of these two cars but with different data so it's fine to keep them

### Missing values (missing values in this dataset have '?' as a place holder)

<table border="1">
  <thead>
    <tr>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model year</th>
      <th>origin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

> Drop missing values

### Data types

<table border="1">
  <thead>
    <tr>
      <th>Variable</th>
      <th>Data Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>mpg</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>cylinders</td>
      <td>int64</td>
    </tr>
    <tr>
      <td>displacement</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>horsepower</td>
      <td>object</td>
    </tr>
    <tr>
      <td>weight</td>
      <td>int64</td>
    </tr>
    <tr>
      <td>acceleration</td>
      <td>float64</td>
    </tr>
    <tr>
      <td>model year</td>
      <td>int64</td>
    </tr>
    <tr>
      <td>origin</td>
      <td>object</td>
    </tr>
  </tbody>
</table>

> Horsepower is converted to float while origin is left as an object because it will be mapped back to numbers to calculate correlation

### Visualization of categorical (discrete) features 

**Bar (count) plot**

![categories_bar_plots](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/ea320f57-ce21-4ab7-b0b3-3f1bb3338c8d)

**Box plot**

![categories_box_plots ](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/5409668b-4c94-4959-abf4-10bb0a8ea4d4)

**Violin plot**

![categories_violin_plots](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/11e9f851-ea16-418c-a62d-d6446d26948e)

**Combined**

![categorical_combined (1)](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/d9476063-4f9b-486d-96c3-fbeaa8063368)

### Visualization of continuous features

**Hist plot**

![continous_hist_plot (1)](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/f6a41cf2-d4e5-41e0-8585-f3cd3b696133)

**Density plot**

![continous_density_plot](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/5a462202-9238-4253-b406-f3e8a98978b6)

**Hist plot with kde curve**

![continous_hist_kde_plot](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/c9eba633-5d9d-4f60-9cb2-882275c54a8a)

### Continuous features descriptive statistics

<table border="1">
  <thead>
    <tr>
      <th></th>
      <th>mpg</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>392.0000</td>
      <td>392.0000</td>
      <td>392.0000</td>
      <td>392.0000</td>
      <td>392.0000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>23.4459</td>
      <td>194.4120</td>
      <td>104.4694</td>
      <td>2977.5842</td>
      <td>15.5413</td>
    </tr>
    <tr>
      <td>std</td>
      <td>7.8050</td>
      <td>104.6440</td>
      <td>38.4912</td>
      <td>849.4026</td>
      <td>2.7589</td>
    </tr>
    <tr>
      <td>min</td>
      <td>9.0000</td>
      <td>68.0000</td>
      <td>46.0000</td>
      <td>1613.0000</td>
      <td>8.0000</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>17.0000</td>
      <td>105.0000</td>
      <td>75.0000</td>
      <td>2225.2500</td>
      <td>13.7750</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>22.7500</td>
      <td>151.0000</td>
      <td>93.5000</td>
      <td>2803.5000</td>
      <td>15.5000</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>29.0000</td>
      <td>275.7500</td>
      <td>126.0000</td>
      <td>3614.7500</td>
      <td>17.0250</td>
    </tr>
    <tr>
      <td>max</td>
      <td>46.6000</td>
      <td>455.0000</td>
      <td>230.0000</td>
      <td>5140.0000</td>
      <td>24.8000</td>
    </tr>
  </tbody>
</table>

### Correlation heatmap

![corr_heatmap](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/a4621ba8-3dc8-497d-b842-efda76a49830)

### Pair plot

![pair_plot](https://github.com/mohdakrory/Deep-Learning-Practice/blob/main/Automobile%20mile%20per%20gallon%20prediction/Data%20description%20and%20visualization/pair_plot.png)

### Pandas profile report 

for more descriptive info on this dataset click [here](https://automobile-mile-per-gallon-prediction.tiiny.site/)

## Feature encoding

### One-hot encoding of origin

<table border="1">
  <tr>
    <th></th>
    <th>is_USA</th>
    <th>is_Europe</th>
  </tr>
  <tr>
    <td>USA</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
    <td>Europe</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Japan</td>
    <td>0</td>
    <td>0</td>
  </tr>
</table>

> Note that these three categories were encoded in 2 columns to avoid the dummy variable trap

<table border="1">
  <thead>
    <tr>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model year</th>
      <th>is_USA</th>
      <th>is_Europe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8</td>
      <td>307.0000</td>
      <td>130</td>
      <td>3504</td>
      <td>12.0000</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>350.0000</td>
      <td>165</td>
      <td>3693</td>
      <td>11.5000</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>318.0000</td>
      <td>150</td>
      <td>3436</td>
      <td>11.0000</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>304.0000</td>
      <td>150</td>
      <td>3433</td>
      <td>12.0000</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>8</td>
      <td>302.0000</td>
      <td>140</td>
      <td>3449</td>
      <td>10.5000</td>
      <td>70</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <!-- ... (add other rows as needed) ... -->
    <tr>
      <td>4</td>
      <td>140.0000</td>
      <td>86</td>
      <td>2790</td>
      <td>15.6000</td>
      <td>82</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>97.0000</td>
      <td>52</td>
      <td>2130</td>
      <td>24.6000</td>
      <td>82</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>4</td>
      <td>135.0000</td>
      <td>84</td>
      <td>2295</td>
      <td>11.6000</td>
      <td>82</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>120.0000</td>
      <td>79</td>
      <td>2625</td>
      <td>18.6000</td>
      <td>82</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>119.0000</td>
      <td>82</td>
      <td>2720</td>
      <td>19.4000</td>
      <td>82</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

## Feature scaling with MinMaxScaler

<table border="1">
  <thead>
    <tr>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model year</th>
      <th>is_USA</th>
      <th>is_Europe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.0000</td>
      <td>0.6176</td>
      <td>0.4565</td>
      <td>0.5361</td>
      <td>0.2381</td>
      <td>0.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1.0000</td>
      <td>0.7287</td>
      <td>0.6467</td>
      <td>0.5897</td>
      <td>0.2083</td>
      <td>0.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1.0000</td>
      <td>0.6460</td>
      <td>0.5652</td>
      <td>0.5169</td>
      <td>0.1786</td>
      <td>0.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1.0000</td>
      <td>0.6098</td>
      <td>0.5652</td>
      <td>0.5160</td>
      <td>0.2381</td>
      <td>0.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>1.0000</td>
      <td>0.6047</td>
      <td>0.5109</td>
      <td>0.5206</td>
      <td>0.1488</td>
      <td>0.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <!-- ... (add other rows as needed) ... -->
    <tr>
      <td>0.2000</td>
      <td>0.1860</td>
      <td>0.2174</td>
      <td>0.3337</td>
      <td>0.4524</td>
      <td>1.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.2000</td>
      <td>0.0749</td>
      <td>0.0326</td>
      <td>0.1466</td>
      <td>0.9881</td>
      <td>1.0000</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <td>0.2000</td>
      <td>0.1731</td>
      <td>0.2065</td>
      <td>0.1934</td>
      <td>0.2143</td>
      <td>1.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.2000</td>
      <td>0.1344</td>
      <td>0.1793</td>
      <td>0.2869</td>
      <td>0.6310</td>
      <td>1.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>0.2000</td>
      <td>0.1318</td>
      <td>0.1957</td>
      <td>0.3139</td>
      <td>0.6786</td>
      <td>1.0000</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>

## Train-Test split 

Train : Test ----> 0.8 : 0.2

## Model Architecture

![model](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/fb0fb4a0-e318-4b80-82ca-0ace351d5526)

## Performance

### Regression metrics on the test set

<table border="1">
  <thead>
    <tr>
      <th>MSE</th>
      <th>MAE</th>
      <th>R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10.7755</td>
      <td>2.5666</td>
      <td>0.8118</td>
    </tr>
  </tbody>
</table>

### Training and validation curves

![Train-Validation_Curves](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/004bbd7c-8612-4760-986d-22c8efec3548)

## Framework diagram

![framework diagram](https://github.com/mohdakrory/Deep-Learning-Practice/assets/67663339/9a598d29-b098-4349-9a32-bc877d149b4d)

