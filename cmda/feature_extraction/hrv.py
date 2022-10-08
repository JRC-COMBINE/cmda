import numpy as np
import pandas as pd

from scipy.signal import welch, periodogram

from ..preprocessing.hrv_preprocessing import (
    rr_rm_outlier,
    rr_rm_ectopic,
    rr_interpolate,
)

from .spectral_features import band_power, band_peak
from .time_domain_features import sample_entropy, perm_entropy
from ..utils.utils import interpolate


def hrv_time_domain_features(x, nan_lim_ratio=0.1):

    nn = x.copy()
    nn = np.asfarray(nn)
    nnd = np.diff(nn)

    num_nan = sum(np.isfinite(nn))

    if (1 - num_nan) < nan_lim_ratio:

        # #SDRR
        # sdrr = np.nanstd(rr)

        # SDNN
        sdnn = np.nanstd(nn)

        # pNN50
        nn50 = np.sum([i > 50 for i in nnd])
        pnn50 = 100 * nn50 / len(nnd)

        # pNN20
        nn20 = np.sum([i > 20 for i in nnd])
        pnn20 = 100 * nn50 / len(nnd)

        # rmssd
        rmssd = np.sqrt(np.nanmean(nnd ** 2))

    else:
        sdnn = np.nan
        pnn50 = np.nan
        pnn20 = np.nan
        rmssd = np.nan

    res = dict(
        sdnn=sdnn,
        pnn50=pnn50,
        pnn20=pnn20,
        rmssd=rmssd
    )

    return res


def hrv_spectral_features(x, fs, win_len, time_stamps, method="cubic"):

    nn =x.copy()
    nn = np.asfarray(nn)

    if np.isfinite(nn).all():
        nn_interpol = interpolate(nn,fs=fs, win_len = win_len, time_stamps=time_stamps, method = method, scale=1000)
        # f,pxx = welch(nn_interpol,fs=fs,window='hamming',nfft=2048, nperseg=512,noverlap=128)
        f,pxx = periodogram(nn,fs=fs, detrend='constant', window='hamming',nfft=2048)
        vlf_power = band_power(
            f=f, pxx=pxx, low=0.003, high=0.04, normalize=False, _dict_out=False
        )

        lf_power = band_power(
            f=f, pxx=pxx, low=0.04, high=0.15, normalize=False, _dict_out=False
        )
        hf_power = band_power(
            f=f, pxx=pxx, low=0.15, high=0.4, normalize=False, _dict_out=False
        )

        total_power = band_power(
            f=f, pxx=pxx, low=0.003, high=0.4, normalize=False, _dict_out=False
        )

        lf_norm = 100*lf_power / (hf_power+lf_power)
        hf_norm = 100*hf_power / (hf_power+lf_power)

        lf_peak = band_peak(f=f, pxx=pxx, low=0.04, high=0.15, _dict_out=False)
        hf_peak = band_peak(f=f, pxx=pxx, low=0.15, high=0.4, _dict_out=False)

        lfhf_ratio = lf_power / hf_power
    else:
        vlf_power = np.nan
        lf_power = np.nan
        hf_power = np.nan
        total_power = np.nan
        lf_peak = np.nan
        hf_peak = np.nan
        lf_norm = np.nan
        hf_norm = np.nan
        lfhf_ratio = np.nan

    res = dict(
        vlf_power=vlf_power,
        lf_power=lf_power,
        hf_power=hf_power,
        total_power = total_power,
        lf_norm=lf_norm,
        hf_norm=hf_norm,
        lf_peak=lf_peak,
        hf_peak=hf_peak,
        lfhf_ratio=lfhf_ratio
    )

    return res


def hrv_nonlinear_features(x,nan_limit_ratio=0.1):

    nan_ratio = 1-(sum(np.isfinite(x))/len(x))
    x = x.copy()
    x = np.asfarray(x)

    if nan_ratio < nan_limit_ratio:
        nn_0 = np.array(x[:-1])
        nn_1 = np.array(x[1:])

        sd1 = np.std(np.subtract(nn_0, nn_1) / np.sqrt(2))
        sd2 = np.std(np.add(nn_0, nn_1) / np.sqrt(2))

        s_area = np.pi * sd1 * sd2

        sd_ratio = sd2 / sd1

        sampent = sample_entropy(x,m=2,_dict_out=False)

        perment = perm_entropy(x,m=3,tau=1,_dict_out=False)

    else:
        sd1 = np.nan
        sd2 = np.nan
        s_area = np.nan
        sd_ratio = np.nan
        sampent = np.nan
        perment = np.nan

    res = dict(
        sd1 = sd1,
        sd2 = sd2,
        s_area = s_area,
        sd_ratio = sd_ratio,
        sample_ent = sampent,
        perm_ent= perment
    )

    return res
