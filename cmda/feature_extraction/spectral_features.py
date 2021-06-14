# Frequency domain features
import numpy as np
from scipy import signal, integrate, stats
import time

def mnf(f,pxx):
    '''
    Compute the mean frequency of a spectrum

    Args:
        f (array_like): Array of sample frequencies
        pxx (array_like): Power spectral density or power spectrum

    Returns:
        float: Mean frequency
    '''    
    
    try:
        res = np.average(f, weights = pxx)
    except:
        res = np.nan

    res = {'mnf':res}
    return res


def mdf(f,pxx):
    '''
    Compute the median frequency of a spectrum

    Args:
        f (array_like): Array of sample frequencies
        pxx (array_like): Power spectral density or power spectrum

    Returns:
        float: Median frequency
    ''' 
    try:
        res = np.min(f[np.cumsum(pxx)>np.sum(pxx)/2])
    except:
        res = np.nan

    res = {'mdf':res}
    return res


def vcf(f,pxx):
    '''
    Compute the variance of central frequency

    Args:
        f (array_like): Array of sample frequencies
        pxx (array_like): Power spectral density or power spectrum

    Returns:
        float: standard deviation frequency
    ''' 
    try:
        avg = np.average(f, weights = pxx)
        res = np.average((f-avg)**2, weights=pxx)
    except:
        res = np.nan

    res = {'vcf':res}
    return res


def stdf(f,pxx):
    '''
    Compute the standard deviation frequency of a spectrum

    Args:
        f (array_like): Array of sample frequencies
        pxx (array_like): Power spectral density or power spectrum

    Returns:
        float: standard deviation frequency
    '''
    variance = vcf(f=f,pxx=pxx)
    res = np.sqrt(variance['vcf'])

    res = {'stdf':res}
    return res


def psr(f,pxx, int_limit_ratio = 0.01):
    try:
        n = int_limit_ratio*np.max(f)
        f0 = f[np.argmax(pxx[1:])+1]
        band_idx = np.logical_and(f >= f0-n , f <= f0+n)
        res = np.sum(pxx[band_idx])/np.sum(pxx)
    except:
        res = np.nan

    res = {f'psr_{int_limit_ratio}':res}
    return res


def peaks(f,pxx,n_peaks =1, height = True, width = True):
    '''
    Args:
        y ([type]): [description]
        x ([type], optional): [description]. Defaults to None.
        n_peaks (int, optional): [description]. Defaults to 1.
        height (bool, optional): [description]. Defaults to True.
        width (bool, optional): [description]. Defaults to True.

    Returns:
        [type]: [description]
    '''
    # find the peaks above the mean value
    peaks_index, peaks = signal.find_peaks(pxx,height=np.quantile(pxx,0.5), width = 0)
    peak_freqs = f[peaks_index]

    # find the highest peaks
    idx = np.argsort(peaks['peak_heights'])[::-1][range(np.min([len(peaks_index),n_peaks]))]

    res = {f'peak_freq_{n+1}':peak_freqs[i] for n,i in enumerate(idx)}
    if height:
        res = {**res,**{f'peak_height_{n+1}':peaks['peak_heights'][i] for n,i in enumerate(idx)}}
    if width:
        res = {**res,**{f'peak_width_{n+1}':peaks['widths'][i] for n,i in enumerate(idx)}}

    return res



def band_power(f,pxx,low = None ,high = None, normalize = True, log = False):
    try:
        _,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
        res= np.sum(band)
        if normalize:
            res = res/np.sum(pxx)
    except:
        res = np.nan

    res = {'band_sum':res}
    return res


def band_std(f,pxx,low = None ,high = None, normalize = True, log = False):
    try:
        _,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
        res= np.std(band)
        if normalize:
            res = res/np.mean(pxx)

        res = {'band_std':res}
    except:
        res = {'band_std':np.nan}

    return res


def band_mnf(f,pxx,low = None ,high = None, log = False):
    
    try:
        f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
        res= mnf(f=f_band,pxx=band)
        res = res['mnf']
    except:
        res = np.nan

    res = {'band_mnf':res}
    return res


def band_mdf(f,pxx,low = None ,high = None, log = False):
    
    try:
        f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
        res= mdf(f=f_band,pxx=band)
        res = res['mdf']
    except:
        res = np.nan

    res = {'band_mnf':res}
    return res



def _band_func(f,pxx,low = None ,high = None,log = False):
    
    if low is None:
        low = min(f)

    if high is None:
        high = max(f)

    band_idx = np.logical_and(f >= low , f <= high)

    if log:
        band = np.log10(pxx[band_idx])
    else:
        band = pxx[band_idx]

    f_band = f[band_idx]
    return f_band,band



def _check_any_nan(x):
    if np.isnan(x).any():
        return True
    if np.isposinf(x).any():
        return True
    if np.isposinf(x).any():
        return True
    return False
        


if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [4,5,3,6,7,5,8,4,1,19,12,23]
    freq = np.array(x)
    pxx = np.array([np.nan,np.nan])
    
    res= band_sum(freq,pxx, low=4, high=6, normalize=False)
    print(res)