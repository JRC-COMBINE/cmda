import numpy as np
import pywt
from scipy import stats
from scipy.signal import periodogram
import cmda.feature_extraction.spectral_features as sf
import cmda.feature_extraction.time_domain_features as tf


def swt_coefficients(x, wavelet, level = 1,_dict_out=True):

    if len(x)%2**level > 0:
        pad = (len(x)//2**level)+1
        pad = pad*2**level
        pad = pad - len(x)
        x_n = np.pad(x,(int(pad/2),int(pad/2)),mode='symmetric')
        padding = True
    else:
        x_n = x.copy()
        padding = False

    coeffs = pywt.swt(
        data = x_n,
        wavelet= wavelet,
        level = level,
        norm = True,
        trim_approx = True
    )
    if padding:
        coeffs = [c[int(pad/2):-int(pad/2)] for c in coeffs]

    if _dict_out:
        coeffs_labels = [f'cA_{level}'] + [f'cD_{l}' for l in np.arange(level,0,-1)]
        res_all = {}
        for c,l in zip(coeffs,coeffs_labels):
            res = {f'swt_{l}' : c}
            res_all = {**res_all,**res}
        coeffs = res_all

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
    
    coeffs = swt_coefficients(x,wavelet=wavelet, level=level, _dict_out=False)
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
            if f == 'see':
                res = tf.entropy(c**2, normalize = True, _dict_out=False)
            elif f == 'mnf':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                res = sf.mnf(freq,pxx,_dict_out=False)
            elif f == 'psr':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                res = sf.psr(freq,pxx,_dict_out=False)
            elif f == 'peak_freq':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                try:
                    res = np.argmax(pxx)
                    res = freq[res]
                except:
                    res = np.nan
            elif f == 'nse':
                freq, pxx = _check_periodogram(c,freq,pxx,fs=fs)
                res = sf.energy(f,pxx,_dict_out=False)
            elif f == 'mds':
                res = np.nanmedian(np.abs(np.diff(c)))*fs
            elif f == 'mns':
                res = np.nanmean(np.diff(c))*fs
            elif f == 'perm_ent':
                res = tf.perm_entropy(c,m=3,tau=1,_dict_out= False)
            else:
                raise ValueError(f'{f} is not in the list of accepted features: {_available_features}')

            res = {f'swt_{l}_{f}' : res}
            res_all = {**res_all,**res}

    return res_all


def _check_periodogram(c,freq,pxx,fs):
    if pxx is None:
        freq, pxx = periodogram(c,fs=fs)
    
    return freq, pxx

            



    