import pandas as pd
import numpy as np

from scipy.interpolate import interp1d

from ..utils.utils import _embed


def rr_scaler(x,factor, **kwargs):
    return factor*np.array(x)

def rr_rm_outlier(x,low=200,high=2500):
    res = np.array([rr if high >= rr >= low else np.nan for rr in x])
    return res

def rr_rm_ectopic(x,k=2,thershold=0.3):
    x = np.array(x)
    m = k*2+1
    padded_x = np.pad(x,k,mode='reflect')
    y = _embed(padded_x,order=m, delay=1)
    outlier_idx = [_ectopic_detect(i,thershold) for i in y]
    x[outlier_idx] = np.nan
    
    return x


def _ectopic_detect(x, thershold):
    j = int((len(x)-1)/2)
    try:
        mean = np.nanmean([x[:j],x[j+1:]])
        diff = abs(x[j]-mean)
        return diff > mean*thershold
    except:
        return False


def rr_interpolate(x, method = 'linear', limit=4, min_samples=200):
    if len(x)>min_samples:
        x = pd.Series(x)
        x.interpolate(method = method, limit=limit, limit_direction='both', inplace = True)
        if method != 'linear':
            x.fillna(method='bfill',limit=limit, inplace=True)
            x.fillna(method='ffill',limit=limit, inplace=True)
    else:
        x = np.repeat(np.nan,len(x))
    return np.array(x)


