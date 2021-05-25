import numpy as np

from scipy import signal
from inspect import getfullargspec

from ._add_filters import _AddFilters
from . import filter_functions as ff


class Filters:

    _udf_list = {}

    _ff_list = [
        'butter_filter',
        'rm_outlier_quantile'
    ]

    def __init__(self):
        self.add = _AddFilters()

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
        res_all = {}

        self._features = {**self.add._ListOfFunctions, **self._udf_list}
        for func_key in self._features:
            args = self._features[func_key]
            func = func_key.split('__')
            counter = func[1]
            func = func[0]
            if func in self._ff_list:
                method_to_call = getattr(ff, func)
                x = method_to_call(x=x, fs=fs,**args)
            elif func_key in self._udf_list:
                # func_name = "_Features" + func
                method_to_call = getattr(self, func_key)
                x = method_to_call(x=x)
            
        return x




def apply_filters(filter_obj, data: dict, fs: int = 1) -> dict:
    """
    Apply filters to a dictionary containing multiple arrays.

    Args:
        filter_obj (python_object): Filter object
        data (dict): Dictionary containing multiple arrays
        fs (int, optional): Sampling frequency of the arrays. Defaults to 1.

    Returns:
        dict: Filtered data.
    """
    if isinstance(filter_obj,dict):
        filters_keys = set(filter_obj.keys())
        data_keys = set(data.keys())
        if len(data_keys.difference(filters_keys)) != 0:
            raise ValueError('The feature object keys are not as same as the data keys')

    res = {}
    for key, x in data.items():
        
        if isinstance(filter_obj,dict):
            obj = filter_obj[key]
        else:
            obj = filter_obj

        
        data[key] = obj.transform(x = x, fs = fs)

    return data



    


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
