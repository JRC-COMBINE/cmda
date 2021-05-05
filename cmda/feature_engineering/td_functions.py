"""
    Built in Time-Domain functions

    Author: Pejman Farhadi Ghalati
"""
import typing

import numpy as np

from scipy import signal, integrate, stats
from math import floor


def _nanfunction(x, func, nanfunc, nan_omit=False, min_samples=1):
    """
    Handle the NaN values in an array when using.

    Args:
        x (array_like): Array containing numbers whose numpy statistic function is desired. 
            If a is not an array, a conversion is attempted.
        func (numpy_function): Numpy statistic function
        nanfunc (numpy_function): Numpy statistic function with ignoring NaN values
        nan_omit (bool, optional): Ignore NaN values in the array. Defaults to False.
        min_samples (int, optional): Minimum number of non-NaN values in the array in order to 
            compute the numpy statistic function. Defaults to 1.

    Returns:
        scaler: Output of either func or nanfunc
    """

    if nan_omit:
        if np.count_nonzero(~np.isnan(x)) >= min_samples:
            out = nanfunc(x)
        else:
            out = np.nan
    else:
        out = func(x)

    return out
