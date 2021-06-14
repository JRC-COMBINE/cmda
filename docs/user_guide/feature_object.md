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
| [`mean`](../api/td_features/mean.md)       | mean |
| [`max`](../api/td_features/max.md)       | maximum |
| [`min`](../api/td_features/min.md)    | minimum |
| [`std`](../api/td_features/std.md)    | standard deviation |
| [`median`](../api/td_features/median.md)    | median |
| [`skewness`](../api/td_features/skewness.md)    | skewness |
| [`kurtosis`](../api/td_features/kurtosis.md)    | kurtosis |
| [`p2p`](../api/td_features/p2p.md)    | peak to peak distance |
| [`rms`](../api/td_features/rms.md)    | root mean square |
| [`zcr`](../api/td_features/zcr.md)    | zero crossing rate                                |

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