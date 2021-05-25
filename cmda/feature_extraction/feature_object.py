import numpy as np

from scipy import signal
from inspect import getfullargspec

from ._add_functions import _AddFeatures
from . import td_functions as td
from . import fd_functions as fd


class Features:

    _udf_list = {}

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
        'zcr'
    ]
    _fd_list = [
        'mnf',
        'mdf',
        'stdf',
        'vcf',
        'psr',
        'peaks',
        'band_sum',
        'band_std',
        'band_mnf',
        'band_mdf',
        'band_stdf'
    ]

    def __init__(self):
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
        self.add = _AddFeatures()

    @classmethod
    def add_udf(cls, func):
        func_name = func.__name__+"__0"

        while func_name in cls._udf_list:
            func_name_splited = func_name.split('__')
            new_func_name = int(func_name_splited[1])+1
            func_name = f'{func.__name__}__{str(new_func_name)}'

        setattr(cls, func_name, decorator_fun(func))
        cls._udf_list = {**cls._udf_list, **{func_name: {}}}


    def transform(self,x,fs):
        '''[summary]

        Args:
            x ([type]): [description]
            fs ([type]): [description]

        Returns:
            [type]: [description]
        '''        
        self.ps = None
        self.freq = None
        self.welch = None
        self.freq_welch = None
        res_all = {}

        self._features = {**self.add._ListOfFunctions, **self._udf_list}
        for func_key in self._features:
            args = self._features[func_key].copy()
            func = func_key.split('__')
            func = func[0]
            if func in self._td_list:
                method_to_call = getattr(td, func)
                res = method_to_call(x=x,**args)
            elif func in self._fd_list:
                method_to_call = getattr(fd, func)
                spectrum = args['spectrum']
                args.pop('spectrum')
                args_list = getfullargspec(method_to_call)[0]
                kwargs = {key: args[key] for key in args.keys() if key not in args_list}
                method_args = {key: args[key] for key in args.keys() if key in args_list}
                f,pxx = self._check_spectrum(x=x,fs=fs,spectrum=spectrum,**kwargs)
                res = method_to_call(f = f, pxx = pxx, **method_args)
            elif func_key in self._udf_list:
                # func_name = "_Features" + func
                method_to_call = getattr(self, func_key)
                res = method_to_call(x=x)
            
            res = _check_duplicated_key_names(res=res,res_all=res_all)
            
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
        list_of_features = {**self.add._ListOfFunctions, **self._udf_list}
        return f"{list_of_features}"

    


def decorator_fun(func):
    # if not isinstance(labels, (list, tuple)):
    #     labels = [labels]

    def wrapper_fun(self,x):
        res = func(x)
        # if not isinstance(res, (list, tuple)):
        #     res = [res]
        # res = dict(zip(labels, res))
        return res

    return wrapper_fun


def _check_duplicated_key_names(res, res_all):

    for k in res.keys():
        key_updated = k
        while key_updated in res_all:
            key_splited = key_updated.split('__')
            try:
                key_updated = int(key_splited[1])+1
                key_updated = f'{k}__{str(key_updated)}'
            except:
                key_updated = f"{k}__2"

        res[key_updated] = res.pop(k)

    return res



if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]

    def fun1(x, y=4):
        return np.min(x), np.std(x)

    def func2(x):
        return np.median(x)

    labels = ("min", "std")

    a = Features()
    a.add_feature.mean()
    a.add_feature.max()
    a.add_fun("udf", fun1, labels)
    a.add_fun("udf_median", func2, "udf_median")
    a.apply_features(x, fs=1)

    print(a._features)
    print(a.features)
