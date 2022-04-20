# Pre-processing

### Filters
```cmda.preprocessing.Filters``` is a tool for appling different filters and outlier reomoval functions on a numeric signal ```x```.

User can select from a number of built-in filters, as well as adding user-defined filters. This functionality makes it possible to tailor the filters based on the application.

Adding the built-in filters is through a dynamic attribute of the ```Filters``` called ```add_udf```. This attribute gives the user access to several built-in signal filters and outlier removal functions.

!!! example
    ```Python
    >>> from cmda.preprocessing import Filters
    >>> filter_obj = Filters()
    >>> filter_obj.add.butter(low=0.5, btype='highpass')
    ```

!!! note
    The order of the added filters to the filter object is important, as the algorithm starts with the first added filtet and goes to the next ones.