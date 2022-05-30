"""
    Built in Time-Domain functions

    Author: Pejman Farhadi Ghalati
"""
import typing
from functools import partial

import numpy as np

from scipy import signal, integrate, stats
from math import floor, factorial
from scipy.interpolate import interp1d

from ..utils.utils import _embed


def _nanfunction(x, func, nanfunc, nan_omit=False, min_samples=1):
    """
    Handle the NaN values in an array, while applying a function.

    Args:
        x (array_like): Array containing numbers whose numpy statistic function is desired.
            If a is not an array, a conversion is attempted.
        func (numpy_function): Numpy statistic function
        nanfunc (numpy_function): Numpy statistic function with ignoring NaN values
        nan_omit (bool, optional): Ignore NaN values in the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN values in the array in order to
            compute the numpy statistic function. Defaults to 1.

    Returns:
        float : Output of either func or nanfunc
    """

    if nan_omit:
        if np.count_nonzero(~np.isnan(x)) >= min_samples:
            res = nanfunc(x)
        else:
            res = np.nan
    else:
        res = func(x)

    return res


def mean(x, nan_omit=False, min_samples=1, _dict_out= True):
    '''
    Compute the average of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose mean is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns returns NaN. Defaults to 1.

    Returns:
        float: the average of x.
    '''
    x = _check_ndarray(x)
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.mean, nanfunc=np.nanmean
    )
    if _dict_out:
        res = {'mean':res}    

    return res


def std(x, nan_omit=False, min_samples=1):
    '''
    Compute the standard deviation of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose standard deviation is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the standard deviation of x.
    '''
    x = _check_ndarray(x)
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.std, nanfunc=np.nanstd
    )
    res = {'std':res}
    return res


def max(x, nan_omit=False, min_samples=1):
    '''
    Compute the maximum value of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose maximum is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the maximum value of x.
    '''
    x = _check_ndarray(x)
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.max, nanfunc=np.nanmax
    )
    res = {'max':res}
    return res


def min(x, nan_omit=False, min_samples=1):
    '''
    Compute the minimum value of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose minimum is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the minimum of x.
    '''
    x = _check_ndarray(x)
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.min, nanfunc=np.nanmin
    )
    res = {'min':res}
    return res


def median(x, nan_omit=False, min_samples=1,_dict_out= True):
    '''
    Compute the median of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose median is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the median of x.
    '''
    x = _check_ndarray(x)
    res = _nanfunction(
        x,
        nan_omit=nan_omit,
        min_samples=min_samples,
        func=np.median,
        nanfunc=np.nanmedian,
    )
    if _dict_out:
        res = {'median':res}
    
    return res


def kurtosis(x, nan_omit=False, min_samples=1):
    '''
    Compute the kurtosis of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose kurtosis is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the kurtosis of x.
    '''
    # create the nankurtosis of stats.kurtosis
    nankurtosis = partial(stats.kurtosis, nan_policy="omit")
    x = _check_ndarray(x)
    res = _nanfunction(
        x,
        nan_omit=nan_omit,
        min_samples=min_samples,
        func=stats.kurtosis,
        nanfunc=nankurtosis,
    )
    res = {'kurtosis':res}
    return res


def skewness(x, nan_omit=False, min_samples=1):
    '''
    Compute the skewness of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose skewness is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the skewness of x.
    '''
    x = _check_ndarray(x)
    if nan_omit:
        if np.count_nonzero(~np.isnan(x)) >= min_samples:
            res = stats.skew(x[~np.isnan(x)])
        else:
            res = np.nan
    else:
        res = stats.skew(x)

    res = {'skewness':res}
    return res


def p2p(x, nan_omit=False, min_samples=1):
    '''
    Compute the peak to peak difference (maximum - minimum values) of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose peak to peak value is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the peak to peak value of x.
    '''
    x = _check_ndarray(x)
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.max, nanfunc=np.nanmax
    ) - _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.min, nanfunc=np.nanmin
    )

    res = {'p2p':res}
    return res


def rms(x, nan_omit=False, min_samples=1):
    '''
    Compute the root means square of the array elements.

    Args:
        x (array_like): 1-D Array containing numbers whose root mean square is desired. 
            If a is not an array, a conversion is attempted.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the root mean square of x.
    '''
    x = _check_ndarray(x)
    res = np.sqrt(_nanfunction(
        x**2, nan_omit=nan_omit, min_samples=min_samples, func=np.mean, nanfunc=np.nanmean
    ))
    res = {'rms':res}
    return res


def zcr(x, center=True, normalized = True, nan_omit=False, min_samples=1):
    '''
    Compute the zero crossing rate of the arary elements.

    The zero-crossing rate (ZCR) is the rate at which an 1-D array changes 
    from positive to zero to negative or from negative to zero to positive.

    Args:
        x (array_like): 1-D Array containing numbers whose zero crossing rate is desired. 
            If a is not an array, a conversion is attempted.
        center (bool, optional): If True, center the array by its mean value, 
            which means the function returns the mean crossing rate of the array. Defaults to True.
        nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, it returns NaN. Defaults to 1.

    Returns:
        float: the mean crossing rate of.
    '''
    # center the x
    x = _check_ndarray(x)
    if center:
        x = x.copy()
        x = x - mean(x,nan_omit=nan_omit, min_samples=min_samples,_dict_out=False)

    res = ((x[:-1] * x[1:]) < 0).sum()

    if normalized:
        total = np.count_nonzero(~np.isnan((x[:-1] * x[1:])))
        res = res/total
        
    res = {'zcr':res}
    return res


def mad(x, nan_omit=False, min_samples=5):
    x = _check_ndarray(x)
    res = x - median(x, nan_omit=nan_omit ,min_samples=min_samples,_dict_out=False)
    res = np.abs(res)
    res = np.median(res)

    res = {'mad':res}
    return res


def entropy(x, normalize = True, _dict_out=True):
    try:
        res = stats.entropy(x, base=2)
        if normalize:
            res /= np.log2(x.size)
    except:
        res = np.nan
    
    if _dict_out:
        res = {'entropy':res}
        
    return res


def perm_entropy(x,m,tau,_dict_out= True):
    x = _check_ndarray(x)
    try:
        x = np.array(x)
    
        hashmult = np.power(m, range(m))

        sorted_idx = _embed(x, order=m, delay=tau).argsort(kind='quicksort')

        hashval = (np.multiply(sorted_idx, hashmult)).sum(1)

        _, c = np.unique(hashval, return_counts=True)

        res = stats.entropy(c, base=2)
        res /= np.log2(factorial(m))
    except:
        res = np.nan

    if _dict_out:
        res = {f'perm_entropy_m{m}_t{tau}':res}

    return res


def sample_entropy(x, m ,std_ratio = 0.2,down_ratio = 0, _dict_out= True):

    x = _check_ndarray(x)
    try:
        n = len(x)

        if down_ratio:
            x = x.copy()
            x = _downsample(x,int(down_ratio*n))

        r = std_ratio*np.std(x)
        # Split time series and save all templates of length m

        x_m = _embed(x,order=m,delay=1)

        # Save all matches minus the self-match, compute B
        b = np.sum([np.sum(np.abs(x_mi - x_m).max(axis=1) <= r) - 1 for x_mi in x_m])
        # Similar for computing A
        x_m = _embed(x,order=m+1,delay=1)
        a = np.sum([np.sum(np.abs(x_mi - x_m).max(axis=1) <= r) - 1 for x_mi in x_m])
        # Return SampEn

        res = -np.log(a / b)

    except:
        res = np.nan

    if _dict_out:
        res = {f'sample_entropy_m{m}':res}
    return res



def periodogram(x, fs=1.0, band=None, window='boxcar', nfft=None, detrend='constant', scaling='density',log=False):

    f,pxx = signal.periodogram(
        x=x,
        fs=fs,
        window=window,
        nfft=nfft,
        detrend=detrend,
        scaling=scaling
    )
    if band is not None:
        band_idx = np.logical_and(f >= band[0] , f <= band[1])
        pxx = pxx[band_idx]
        f = f[band_idx]

    if log:
        pxx = np.log10(pxx)

    res = {f'ps_{i}_Hz':j for i,j in zip(f,pxx)}
    return res


def welch(x, fs=1.0, band=None, window='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', scaling='density', average='mean', log=False):

    f,pxx = signal.welch(
        x=x,
        fs=fs,
        window=window,
        nperseg=nperseg,
        noverlap=noverlap,
        nfft=nfft,
        detrend=detrend,
        scaling=scaling,
        average=average
    )

    if band is not None:
        band_idx = np.logical_and(f >= band[0] , f <= band[1])
        pxx = pxx[band_idx]
        f = f[band_idx]

    if log:
        pxx = np.log10(pxx)

    res = {f'welch_{i}_Hz':j for i,j in zip(f,pxx)}
    return res

#TODO auto correlation must be fixed
def autocorr(x,fs,center = True):
    pass



def _check_ndarray(x):
    if isinstance(x,np.ndarray):
        return x
    return np.array(x)



def _downsample(array, npts):
    interpolated = interp1d(np.arange(len(array)), array, axis = 0, fill_value = 'extrapolate')
    downsampled = interpolated(np.linspace(0, len(array), npts))
    return downsampled


if __name__ == "__main__":
    x = (12,10,8,14,9,8,6)
    print(perm_entropy(x,3,1))

    y = (2/5*(np.log2(1/5)))+(3/5*np.log2(3/5))
    print(-y/np.log2(6))