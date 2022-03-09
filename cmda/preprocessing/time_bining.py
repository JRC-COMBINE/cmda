import numpy as np
import pandas as pd

from scipy.interpolate import interp1d

def interpolate(x,t, win_len, fs, method='linear'):

    t_interpol = np.arange(0,win_len,1/fs)
    idx_finite = np.isfinite(x)
    f_interpol = interp1d(t[idx_finite], x[idx_finite], kind=method ,bounds_error=False)
    x_interpol = f_interpol(t_interpol)

    x_interpol = pd.Series(x_interpol)
    x_interpol.fillna(method='bfill',inplace=True)
    x_interpol.fillna(method='ffill',inplace=True)

    res = np.array(x_interpol)

    return x_interpol