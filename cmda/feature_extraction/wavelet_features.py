import numpy as np
import pywt
from scipy import stats
from scipy.signal import periodogram
import cmda.feature_extraction.spectral_features as sf
import cmda.feature_extraction.time_domain_features as tf


def swt(x, wavelet, level = 1, start_level = 0):

    max_level = start_level + level

    max_len = len(x)-len(x)%2**max_level
    coeffs = pywt.swt(
        data = x[:max_len],
        wavelet= wavelet,
        level = level,
        start_level = start_level,
        norm = True,
        trim_approx = True
    )

    return coeffs


def swt_features(x,features,fs,wavelet, level, start_level = 1, rm_cA = False,**kwargs):
    _available_features = [
        'mean',
        'std',
        'kurt',
        'skew',
        'rms',
        'p2p',
        'mean_freq'
    ]
    
    coeffs = swt(x,wavelet=wavelet, level=level)
    coeffs_labels = [f'cA_{level}'] + [f'cD_{l}' for l in np.arange(level,0,-1)]
    if start_level > 1:
        if start_level > level:
            raise ValueError('start level must be smaller than the level value')
        else:
            coeffs = coeffs[:-(start_level-1)]
            coeffs_labels = coeffs_labels[:-(start_level-1)]

    if rm_cA:
        coeffs = coeffs[1:]
        coeffs_labels = coeffs_labels[1:]

    res_all = {}
    for c,l in zip(coeffs,coeffs_labels):
        pxx = None
        freq = None
        for f in features:
            if f == 'mean':
                res = np.mean(c)
            elif f == 'std':
                res = np.std(c)
            elif f == 'kurt':
                res = stats.kurtosis(c)
            elif f == 'skew':
                res = stats.skew(c)
            elif f == 'p2p':
                res = np.max(c) - np.min(c)
            elif f == 'rms':
                res = np.sqrt(np.mean(c**2))
            elif f == 'mnf':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                res = sf.mnf(freq,pxx,_dict_out=False)
            elif f == 'mdf':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                res = sf.mdf(freq,pxx,_dict_out=False)
            elif f == 'peak_freq':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                try:
                    res = np.argmax(pxx)
                    res = freq[res]
                except:
                    res = np.nan
            elif f == 'normalized_power':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                res = np.nansum(np.array(pxx)**2)/len(pxx)

            elif f == 'mds':
                res = np.nanmedian(np.abs(np.diff(c)))*fs
            elif f == 'sample_entropy':
                res = tf.sample_entropy(c,m=2,tau=1,down_ratio=0.2, _dict_out=False)
            else:
                raise ValueError(f'{f} is not in the list of accepted features: {_available_features}')

            res = {f'swt_{l}_{f}' : res}
            res_all = {**res_all,**res}

    return res_all


def _check_periodogram(c,freq,pxx,fs):
    if pxx is None:
        freq, pxx = periodogram(c,fs=fs)
    
    return freq, pxx

            



    