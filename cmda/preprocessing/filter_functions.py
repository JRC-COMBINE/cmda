import numpy as np
from scipy import signal

def butter_filter(x,fs,cutoff, order = 4, btype = 'lowpass'):
    '''
    Apply Buuterworth filter to an array elements

    Args:
        x (array_like): 1-D array or object that can be converted to an array.
        fs (float, optional): Sampling frequency
        cutoff (float): Cutoff frequency [Hz].
        order (int, optional): The order of the filter. Defaults to 4.
        btype ({‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}, optional): Defaults to 'lowpass'.

    Returns:
        ndarray: filtered array
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
        x (array_like): 1-D array or object that can be converted to an array
        fs (float, optional): Sampling frequency
        q_up (float, optional): Upper quantile
        q_low (float, optional): lower quantile

    Returns:
        ndarray: Filtered array
    '''    
    quantiles = x.quantile([q_up, q_low]).values
    x[x < quantiles[0]] = quantiles[0]
    x[x > quantiles[1]] = quantiles[1]

    return x



def rm_outlier_std(x, low, high, win_len, step, nan_limit = 0.1):
    # BP: low =2, high: 30
    # ECG: low = 0.05, high = 1.5 
    bins = get_bins(n = len(x), win_len=win_len, step = step, fs=fs)
    nan_bins = [i for i in bins if np.isnan(x[i]).any() or (np.std(x[i])<low or np.std(x[i]>high))]
    ratio = len(nan_bins)/len(bins)
    if ratio>0:
        for i in nan_bins:
            x[i] = np.nan
    if ratio<nan_limit:
        x = x[~np.isnan(x)]

    return x

