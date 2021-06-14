"""
    Built in Time-Domain functions

    Author: Pejman Farhadi Ghalati
"""
import typing
from functools import partial

import numpy as np

from scipy import signal, integrate, stats
from math import floor


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


def mean(x, nan_omit=False, min_samples=1):
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
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.mean, nanfunc=np.nanmean
    )
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
    res = _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.min, nanfunc=np.nanmin
    )
    res = {'min':res}
    return res


def median(x, nan_omit=False, min_samples=1):
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
    res = _nanfunction(
        x,
        nan_omit=nan_omit,
        min_samples=min_samples,
        func=np.median,
        nanfunc=np.nanmedian,
    )
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
    res = np.sqrt(_nanfunction(
        x**2, nan_omit=nan_omit, min_samples=min_samples, func=np.mean, nanfunc=np.nanmean
    ))
    res = {'rms':res}
    return res


def zcr(x, center=True, nan_omit=False, min_samples=1):
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
    x = _check_ndarray(x).copy()

    if center:
        x -= _nanfunction(
        x, nan_omit=nan_omit, min_samples=min_samples, func=np.mean, nanfunc=np.nanmean
    )

    res = ((x[:-1] * x[1:]) < 0).sum()
    res = {'zcr':res}
    return res


#TODO auto correlation must be fixed
def autocorr(x,fs,center = True):
    pass



def _check_ndarray(x):
    if isinstance(x,np.ndarray):
        return x
    return np.array(x)