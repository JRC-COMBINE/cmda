import numpy as np
import pywt
from scipy import stats
from scipy.signal import periodogram


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


def swt_features(x,features,wavelet, level, start_level = 1,**kwargs):
    _available_features = [
        'mean',
        'var',
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
            raise ValueError('start level must be smaller than the level valye')
        else:
            coeffs = coeffs[:-(start_level-1)]
            coeffs_labels = coeffs_labels[:-(start_level-1)]

    res_all = {}
    for c,l in zip(coeffs,coeffs_labels):
        for f in features:
            if f == 'mean':
                res = np.mean(c)
            elif f == 'var':
                res = np.var(c)
            elif f == 'kurt':
                res = stats.kurtosis(c)
            elif f == 'skew':
                res = stats.skew(c)
            elif f == 'p2p':
                res = np.max(c) - np.min(c)
            elif f == 'rms':
                res = np.sqrt(np.mean(c**2))
            else:
                raise ValueError(f'{f} is not in the list of accepted features: {_available_features}')

            res = {f'swt_{l}_{f}' : res}
            res_all = {**res_all,**res}

    return res_all




            



    