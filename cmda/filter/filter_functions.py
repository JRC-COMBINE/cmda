import numpy as np
from scipy import signal

def butter_filter(x,fs,cutoff, order = 4, btype = 'lowpass'):
    '''
    Apply Buuterworth filter to an array.

    Args:
        x (array_like): 1-D array to be filtered.
        fs (float): Sampling frequency of the x time series. Defaults to 1.0.
        cutoff ([type]): cutoff frequency of the butterworth filter
        order (int, optional): [description]. Defaults to 4.
        btype (str, optional): {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}; The type of filter. Defaults to 'lowpass'.

    Returns:
        ndarray, same shape as x: The filtered array.
    '''
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(N = order, Wn = normal_cutoff, btype= btype, analog=False)
    # create the filter using the defined Butterworth
    res = signal.filtfilt(b, a, x)

    return res


def rm_outliers_quantile(x, fs =1, q_up = 1, q_low = 0):
    '''
    Remove the q-th quantile of an array as outliers.

    Args:
        x (array_like): 1-D array or object that can be converted to an array.
        fs (float, optional): Sampling frequency
        q_up (float, optional): Upper quantile
        q_low (float, optional): lower quantile

    Returns:
        [ndarray]: Filtered array.
    '''    

    quantiles = x.quantile([q_up, q_low]).values
    x[x < quantiles[0]] = quantiles[0]
    x[x > quantiles[1]] = quantiles[1]

    return x


