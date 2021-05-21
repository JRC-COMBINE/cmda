import numpy as np

def add2list(func):
    def wrapper(self,**kwargs):

        args = func(self,**kwargs)

        func_name = func.__name__+"__0"

        while func_name in self._ListOfFunctions:
            func_name_splited = func_name.split('__')
            new_func_name = int(func_name_splited[1])+1
            func_name = f'{func.__name__}__{str(new_func_name)}'

        self._ListOfFunctions[func_name] = args

    return wrapper


def _get_args(args):
    args.pop('self')
    if 'kwargs' in args.keys():
        kwargs = args.pop('kwargs')
        args = {**args,**kwargs}
    return args


class _AddFeatures:
    def __init__(self):
        self._ListOfFunctions = {}

    @add2list
    def mean(self, nan_omit=True, min_samples=1):
        """
        Add the "mean" function to the features.
        The feature object returns the average of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        return _get_args(locals())

    @add2list
    def max(self, nan_omit=True, min_samples=1):
        """
        Add the "max" function to the features.
        The feature object returns the maximum value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        return _get_args(locals())

    @add2list
    def min(self, nan_omit=True, min_samples=1):
        """
        Add the "min" function to the features.
        The feature object returns the minimum value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        return _get_args(locals())

    @add2list
    def std(self, nan_omit=True, min_samples=5):
        """
        Add the "std" function to the features.
        The feature object returns the standard deviation of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        return _get_args(locals())

    @add2list
    def median(self, nan_omit=True, min_samples=5):
        """
        Add the "median" function to the features.
        The feature object returns the median value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        return _get_args(locals())

    @add2list
    def kurtosis(self, nan_omit=True, min_samples=5):
        """
        Add the "kurtosis" function to the features.
        The feature object returns the kurtosis of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        return _get_args(locals())

    @add2list
    def skewness(self, nan_omit=True, min_samples=5):
        """
        Add the "skewness" function to the features.
        The feature object returns the skewness of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        return _get_args(locals())

    @add2list
    def p2p(self, nan_omit=True, min_samples=1):
        """
        Add the "p2p" function to the features.
        The feature object returns the peak to peak value of the array elements.
        peak to peak (p2p) is the difference of the maxumum and minimum values of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        return _get_args(locals())

    @add2list
    def rms(self, nan_omit=True, min_samples=5):
        """
        Add the "rms" function to the features.
        The feature object returns the root mean square of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        return _get_args(locals())

    @add2list
    def zcr(self, center=True, nan_omit=True, min_samples=1):
        """
        Add the "zcr" function to the features.
        The feature object returns the zero crossing rate of the array elements.

        Args:
            center (bool, optional): If True, center the array by its mean value, 
                which means the function returns the mean crossing rate of the array. Defaults to True.
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        return _get_args(locals())


    @add2list
    def mnf(self,spectrum='ps',**kwargs):
        return _get_args(locals())

    @add2list
    def mdf(self,spectrum='ps',**kwargs):
        return _get_args(locals())

    @add2list
    def stdf(self,spectrum='ps',**kwargs):
        return _get_args(locals())

    @add2list
    def vcf(self,spectrum='ps',**kwargs):
        return _get_args(locals())

    @add2list
    def psr(self,spectrum='ps',int_limit_ratio = 0.01,**kwargs):
        return _get_args(locals())

    @add2list
    def peaks(self,spectrum='ps',n_peaks =1, height = True, width = True,**kwargs):
        return _get_args(locals())

    @add2list
    def band_sum(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        return _get_args(locals())

    @add2list
    def band_std(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        return _get_args(locals())

    @add2list
    def band_mnf(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        return _get_args(locals())

    @add2list
    def band_mdf(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        return _get_args(locals())

    @add2list
    def band_stdf(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        return _get_args(locals())






