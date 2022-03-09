
import numpy as np
import pandas as pd

from scipy.interpolate import interp1d

def _embed(x, order=3, delay=1):
    """Time-delay embedding.
    Parameters
    ----------
    x : 1d-array
        Time series, of shape (n_times)
    order : int
        Embedding dimension (order).
    delay : int
        Delay.
    Returns
    -------
    embedded : ndarray
        Embedded time-series, of shape (n_times - (order - 1) * delay, order)
    """
    N = len(x)
    if order * delay > N:
        raise ValueError("Error: order * delay should be lower than x.size")
    if delay < 1:
        raise ValueError("Delay has to be at least 1.")
    if order < 2:
        raise ValueError("Order has to be at least 2.")
    Y = np.zeros((order, N - (order - 1) * delay))
    for i in range(order):
        Y[i] = x[i * delay:i * delay + Y.shape[1]]
    return Y.T



def interpolate(x,fs,win_len,time_stamps,method='linear',scale=1000):
    
    # t = np.cumsum(x)
    # t = t - t[0]
    try:
        f_interpol = interp1d(time_stamps, x, kind=method, bounds_error=False)
    except ValueError:
        x, time_stamps = _remove_duplicated_timestamps(x,time_stamps)
        f_interpol = interp1d(time_stamps, x, kind=method, bounds_error=False)

    t_interpol = np.arange(0, scale*win_len, scale / fs)

    x_interpol = f_interpol(t_interpol)

    x_interpol = pd.Series(x_interpol)
    x_interpol.fillna(method='bfill',inplace=True)
    x_interpol.fillna(method='ffill',inplace=True)

    res = np.array(x_interpol)

    return res


def _remove_duplicated_timestamps(x,t):
    idx = np.array([0])
    while idx.size>0:
        _,count = np.unique(t, return_counts=True)
        idx = np.where(count>1)[0]
        x = np.delete(x,idx)
        t = np.delete(t,idx)
    
    return x,t