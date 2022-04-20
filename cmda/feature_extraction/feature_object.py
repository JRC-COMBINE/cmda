import numpy as np
import inspect

from scipy import signal
from inspect import getfullargspec

from ._add_functions import _AddFeatures
from ..utils.utils import _AddUDF
from ..utils.checks import _check_duplicated_key_names
from . import time_domain_features as td
from . import spectral_features as fd
from . import wavelet_features as wf
from . import hrv


class Features:

    _td_list = [
        'mean',
        'max',
        'min',
        'median',
        'std',
        'skewness',
        'kurtosis',
        'rms',
        'p2p',
        'zcr',
        'perm_entropy',
        'sample_entropy'
    ]

    _ps_list = [
        'periodogram',
        'welch'
    ]

    _fd_list = [
        'mnf',
        'mdf',
        'stdf',
        'vcf',
        'psr',
        'peaks',
        'band_power',
        'band_std',
        'band_mnf',
        'band_mdf',
        'band_stdf',
        'band_agg',
        'spectral_entropy'
    ]

    _wf_list = [
        'swt_features'
    ]

    _hrv_list = [
        'hrv_time_domain_features',
        'hrv_nonlinear_features'
    ]

    _hrvf_list = [
        'hrv_spectral_features',
    ]

    def __init__(self,udf_source=None):
        '''
        Create a Feature object for extracting features from an array.
        Built-in features can be added by the "add" function.

        Read more in the [User Guide](../user_guide/feature_object.ipynb).

        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,3,4,5,6,7,8]
            >>> feature_obj = Features()
            >>> feature_obj.add.mean()
            >>> feature_obj.add.max()
            >>> feature_obj.add.std()
            >>> res = feature_obj.transform(x=x,fs=1)

        '''
        # _AddFeatures for calling the built-in functions        
        self.add = _AddFeatures()

        # _AddUDF  for adding the user-defined functions
        self.udf = _AddUDF()


    def transform(self,x,fs=1, **kwargs):
        '''
        apply the added feature functions to the array `x`

        Args:
            x (array-like): Input array
            fs (float,optional): Sampling frequency of `x`. Defaults to 1.

        Returns:
            dict: extracted features from `x`
        '''

        # create a buffer for the periodogram and welch spectrum    
        self.ps = None
        self.freq = None
        self.welch = None
        self.freq_welch = None

        # pre-define the final result as a dict 
        res_all = {}

        # run a for loop on the added built-in features
        for func_key in self.add._ListOfFunctions:

            # get the args of the built-in funtion
            args = self.add._ListOfFunctions[func_key].copy()
            func = func_key.split('__')
            func = func[0]

            # check whether the function name is in the time-domain features
            if func in self._td_list:
                method_to_call = getattr(td, func)
                res = method_to_call(x=x,**args)
            # check whether the function name is a power spectrum function
            elif func in self._ps_list:
                method_to_call = getattr(td, func)
                res = method_to_call(x=x,fs=fs,**args)
            # check whether the function name is in hrv time domain and non-linear features
            elif func in self._hrv_list:
                method_to_call = getattr(hrv, func)
                res = method_to_call(x=x,**args)
            # check whether the function name is hrv frequency-domain features
            elif func in self._hrvf_list:
                method_to_call = getattr(hrv, func)
                res = method_to_call(x=x,**args,**kwargs)
            # check whether the function name is a wavelet features
            elif func in self._wf_list:
                method_to_call = getattr(wf, func)
                res = method_to_call(x=x,fs=fs,**args)
            # check whether the function name is a frequency-domain feature
            elif func in self._fd_list:
                method_to_call = getattr(fd, func)
                spectrum = args['spectrum']
                args.pop('spectrum')
                args_list = getfullargspec(method_to_call)[0]
                kwargs = {key: args[key] for key in args.keys() if key not in args_list}
                method_args = {key: args[key] for key in args.keys() if key in args_list}

                # check whether the power spectrum exists in the buffer
                f,pxx = self._check_spectrum(x=x,fs=fs,spectrum=spectrum,**kwargs)
                res = method_to_call(f = f, pxx = pxx, **method_args)
            
            # handle duplicated function names
            res_all = {**res_all, **res}

        for func_key in self.udf._ListOfUDFs:
            args = self.udf._ListOfUDFs[func_key].copy()
            # func = func_key.split('__')
            # func = func[0]
            method_to_call = getattr(self.udf, func_key)
            res = method_to_call(x=x)

            # handle duplicated function names
            res_all = {**res_all, **res}

    
        return res_all


    def _check_spectrum(self,spectrum,x,fs,**kwargs):
        if spectrum == 'ps':
            if self.ps is None:
                f, pxx = signal.periodogram(x, fs=fs, **kwargs)
                self.ps = pxx
                self.freq = f
            else:
                f = self.freq
                pxx = self.ps
        elif spectrum == 'welch':
            if self.welch is None:
                f, pxx = signal.welch(x, fs=fs, **kwargs)
                self.welch = pxx
                self.freq_welch = f
            else:
                f = self.freq_welch
                pxx = self.welch

        return f,pxx


    def __str__(self):
        list_of_features = {**self.add._ListOfFunctions, **self.udf._ListOfUDFs}
        return f"{list_of_features}"

    






