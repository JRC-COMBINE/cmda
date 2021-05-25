# Feature Object

### Features
```cmda.feature_extraction.Features``` is a tool for extracting multiple features at the same time from a numeric signal ```x```.

User can select from a wide variety of built-in features, as well as adding user-defined features. This functionality makes it possible to tailor the features based on the application.

Adding the built-in features is through a dynamic attribute of the Features called ```add```. This attribute gives the user access to several built-in time-domain, frequency-domain and/or wavelet features.

!!! example
    ```Python
    >>> from cmda.feature_extraction import Features
    >>> feature_obj = Features()
    >>> feature_obj.add.mean()
    ```


A list of all the available features can be seen in the following tables:

### Time-domain Features
| Feature     | Description                          |
| :-----------: | :------------------------------------: |
| `mean`       | mean |
| `max`       | maximum |
| `min`    | minimum |
| `std`    | standard deviation |
| `median`    | median |
| `skewness`    | skewness |
| `kurtosis`    | kurtosis |
| `p2p`    | peak to peak distance |
| `rms`    | root mean square |
| `zcr`    | zero crossing rate                                |

### Frequency-domain Features
| Feature     | Description                          |
| :-----------: | :------------------------------------: |
| [`mnf`](../api/fd_features/mnf.md)       | mean frequency |
| [`mdf`](../api/fd_features/mdf.md)       | median frequency |
| `vcf`    | variance of central frequency |
| `stdf`    | standard deviation of central frequency |
| `psr`    | power spectral ratio |
| `peaks`    | peaks of spectrum |
| `band_sum`    | energy of a spectrum band |
| `band_std`    | power standard deviation of a spectrum band |
| `band_mnf`    | mean frequency of a spectrum band |
| `band_mdf`    | median frequency of a spectrum band |
| `band_stdf`    | standard deviation of central frequency of a spectrum band|

### Example
A complete tutorial of implementing the feature object can be found [here](../examples/feature_object.ipynb)