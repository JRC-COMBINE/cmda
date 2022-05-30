# Feature Extraction

Generally, feature extraction or engineering can be described as a time series data representation via a set of features that correspond to the temporal data characteristic or pattern. Additionally, feature extraction is typically a procedure that reduces the dimensionality of an input signal or compresses its data and accordingly reduces the number of resources needed to analyze it.

## Features
```cmda.feature_extraction.Features``` is a tool for extracting multiple features from a numeric signal ```x```.

User can select from a wide variety of built-in features, as well as adding user-defined features. This functionality makes it possible to tailor the features based on the application.

Adding the built-in features is through a dynamic attribute of the Features called ```.add```. This attribute gives the user access to several built-in time-domain, spectral features, and wavelet features.
All the built-in functions are created using ```NumPy``` and ```SciPy``` APIs.

!!! example
    ```Python
    >>> from cmda.feature_extraction import Features
    >>> feature_obj = Features()
    >>> feature_obj.add.mean()
    ```


### Time-domain Features
Time-domain features are the temporal data descriptors in a time analysis span. The following table shows the most common and popular time-domain features used in time-series data analysis:

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
| [`zcr`](../api/td_features/zcr.md)    | zero crossing rate|


### Frequency-domain Features
Frequency-domain features are signal characteristics in the frequency domain, which
are extracted from the Fourier transform of the signal.
The following table shows the most common and popular frequency-domain features used in time-series data analysis:

| Feature     | Description                          |
| :-----------: | :------------------------------------: |
| [`mnf`](../api/fd_features/mnf.md)       | mean frequency |
| [`mdf`](../api/fd_features/mdf.md)       | median frequency |
| [`vcf`](../api/fd_features/vcf.md)     | variance of central frequency |
| [`stdf`](../api/fd_features/stdf.md)     | standard deviation of central frequency |
| [`psr`](../api/fd_features/psr.md)     | power spectral ratio |
| [`peaks`](../api/fd_features/peaks.md)     | peaks of spectrum |
| [`band_power`](../api/fd_features/band_power.md)     | energy of a spectrum band |
| [`band_std`](../api/fd_features/band_std.md)    | power standard deviation of a spectrum band |
| [`band_mnf`](../api/fd_features/band_mnf.md)    | mean frequency of a spectrum band |
| [`band_mdf`](../api/fd_features/band_mdf.md)    | median frequency of a spectrum band |
| [`band_stdf`](../api/fd_features/band_std.md)    | standard deviation of central frequency of a spectrum band|
| [`band_agg`](../api/fd_features/band_agg.md)    | a summerized of features values of a spectrum band|

### Entropy Features
Shannon entropy measures information and irregularity in a random variable in information theory. The potential benefit of Shannon entropy in determining the complexity of temporal data led to the definition of various forms of entropy that we can derive as time-series data features.
The following table shows the most common entropy features used in time-series data analysis:

| Feature     | Description                          |
| :-----------: | :------------------------------------: |
| [`sample_entropy`](../api/entropy_features/sample_entropy.md)       | Sample Entropy |
| [`perm_entropy`](../api/entropy_features/perm_entropy.md)       | Permutation Entropy |
| [`spectral_entropy`](../api/entropy_features/spectral_entropy.md)     | Spectral Entropy |


### Stationary Wavelet Features
Stationary wavelet transform is an alternative wavelet transform developed to restore the translation invariance in Discrete Wavelet Transform (DWT).
SWT offers a handful of features that can be extracted from the transformation coefficients using the following function:

| Feature     | Description                          |
| :-----------: | :------------------------------------: |
| [`swt_features`](../api/fd_features/swt_features.md)       | SWT Coefficients Features |

### User-Defined Functions
Users can define and add their functions to the Features object instance via ```.udf.add```.

### Example
A complete tutorial of implementing the feature object can be found [here](../examples/feature_object.ipynb)