# Frequency domain features
import numpy as np
from scipy import signal, integrate, stats
import time

def energy(f,pxx,_dict_out=True):
    try:
        res = np.sum(pxx)
    except:
        res = np.nan

    if _dict_out:
        res = {'energy':res}
    return res

def mnf(f,pxx, _dict_out = True):
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

    if _dict_out:
        res = {'mnf':res}
    return res


def mdf(f,pxx,_dict_out=True):
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

    if _dict_out:
        res = {'mdf':res}
    return res


def vcf(f,pxx,_dict_out=True):
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

    if _dict_out:
        res = {'vcf':res}

    return res


def stdf(f,pxx,_dict_out=True):
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

    if _dict_out:
        res = {'stdf':res}

    return res


def psr(f,pxx, int_limit_ratio = 0.01,_dict_out=True):
    try:
        n = int_limit_ratio*np.max(f)
        f0 = f[np.argmax(pxx[1:])+1]
        band_idx = np.logical_and(f >= f0-n , f <= f0+n)
        res = np.sum(pxx[band_idx])/np.sum(pxx)
    except:
        res = np.nan

    if _dict_out:
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



def band_power(f,pxx,low = None ,high = None, normalize = True, log = False, _dict_out=True):
    try:
        f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
        df = f_band[1]-f_band[0]
        res= np.sum(band) * df
        if normalize:
            res = res/(np.sum(pxx)*df)
    except:
        res = np.nan

    if _dict_out:
        res = {f'power_[{low},{high}]Hz':res}

    return res



def band_mnf(f,pxx,low = None ,high = None, log = False,_dict_out=True):

    f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
    res= mnf(f=f_band,pxx=band,_dict_out=False)

    if _dict_out:
        res = {f'mnf_[{low},{high}]Hz':res}

    return res


def band_mdf(f,pxx,low = None ,high = None, log = False,_dict_out=True):
    
    f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
    res= mdf(f=f_band,pxx=band,_dict_out=False)

    if _dict_out:
        res = {f'mdf_[{low},{high}]Hz':res}

    return res

def band_peak(f,pxx,low = None ,high = None, log = False,_dict_out=True):

    f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
    argmax = np.argmax(band)
    res = f_band[argmax]

    if _dict_out:
        res = {f'freq_peak_[{low},{high}]Hz':res}

    return res

def band_entropy(f,pxx,low = None ,high = None, log = False,_dict_out=True):
    
    f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)
    res = spectral_entropy(f=f_band,pxx=band,_dict_out=False)

    if _dict_out:
        res = {f'entropy_[{low},{high}]Hz':res}

    return res


def band_agg(f,pxx,low = None ,high = None, log = False):
    
    f_band,band = _band_func(f=f, pxx=pxx, low=low, high=high, log = log)


    mnf_res = mnf(f=f_band,pxx=band,_dict_out=False)
    vcf_res = vcf(f=f_band,pxx=band,_dict_out=False)
    argmax = np.argmax(band)
    peak = f_band[argmax]
    entropy = spectral_entropy(f=f_band,pxx=band,_dict_out=False)
    try:
        power = np.sum(band) * (f_band[1]-f_band[0])
        power = power/(np.sum(pxx) * (f[1]-f[0]))
    except:
        power = np.nan

    res = {
        f'power_[{low},{high}]Hz':power,
        f'mnf_[{low},{high}]Hz':mnf_res,
        f'vcf_[{low},{high}]Hz':vcf_res,
        f'peak_[{low},{high}]Hz':peak,
        f'entropy_[{low},{high}]Hz':entropy
    }
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


def spectral_entropy(f,pxx,normalized=True, _dict_out=True):
    try:
        res = stats.entropy(pxx, base=2)
        if normalized:
            res /= np.log2(pxx.size)
    except:
        res = np.nan

    if _dict_out:
        res = {'spectral_entropy':res}
    return res

def _check_any_nan(x):
    if np.isnan(x).any():
        return True
    if np.isposinf(x).any():
        return True
    if np.isposinf(x).any():
        return True
    return False
        


