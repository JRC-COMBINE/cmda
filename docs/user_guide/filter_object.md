# Pre-processing

### Filters
```cmda.preprocessing.Filters``` is a tool for appling different filters and outlier reomoval functions on a numeric signal ```x```.

User can select from a number of built-in filters, through a dynamic attribute of the Filters object, called ```.add``` that gives the user access to the following functions:

| Feature     | Description                          |
| :-----------: | :------------------------------------: |
| [`scaler`](../api/preprocessing/scaler.md)       | Scaler |
| [`rm_outlier`](../api/preprocessing/rm_outlier.md)       | Remove ouliers by cutoffs |
| [`rm_outlier_quantile`](../api/preprocessing/rm_outlier_quantile.md)     | Remove ouliers by quantile cutoffs |
| [`butter_filter`](../api/preprocessing/butter.md)     | Butterworth bandpass filter |
| [`interpolate_na`](../api/preprocessing/scaler.md)     | Interpolate missing values |

All the built-in functions are created using ```NumPy``` and ```SciPy``` APIs.

Users can define and add their prerocessing functions to the Filters object instance via ```.udf.add```.

!!! example
    ```Python
    >>> from cmda.preprocessing import Filters
    >>> filter_obj = Filters()
    >>> filter_obj.add.butter(low=0.5, btype='highpass')
    ```

!!! note
    The order of the added filters to the filter object is important, as the algorithm starts with the first added filtet and goes to the next ones.