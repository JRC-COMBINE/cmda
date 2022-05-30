import numpy as np



def _get_args(args):
    args.pop('self')
    if 'kwargs' in args.keys():
        kwargs = args.pop('kwargs')
        args = {**args,**kwargs}
    return args


class _AddFilters:
    def __init__(self):
        self._ListOfFunctions = {}

    def _add2list(self,args,func_name):
        func_name_ = func_name+"__0"

        while func_name_ in self._ListOfFunctions:
            func_name_splited = func_name_.split('__')
            new_func_name = int(func_name_splited[1])+1
            func_name_ = f'{func_name}__{str(new_func_name)}'

        self._ListOfFunctions[func_name_] = args


    def rm_outlier(self, low=None, high=None):
        '''
        Remove outliers using a low and high cutoffs

        Args:
            low (float,optional): The cutoff, that all values below will be removed. If set to None, no cutoff is applied. Defaults to None.
            high (float,optional): The cutoff, that all values above will be removed. Defaults to None.
        Returns:
            ndarray: filtered array
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='rm_outlier')

    def rm_outlier_quantile(self, q_up = 1, q_low = 0):
        '''
        Remove outliers using the a low and high quantiles of the array as cutoffs

        Args:
            q_low (float,optional): Quantile that defines the lower cutoff, which must be between 0 and 1. Defaults to 0.
            q_up (float,optional): Quantile that defines the higher cutoff, which must be between 0 and 1. Defaults to 1.
        Returns:
            ndarray: filtered array
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='rm_outlier')


    def interpolate_na(self,method = 'linear', limit=4):
        '''
        Fill NaN values using an interpolation method using ```pandas.Series.interpolate```

        Args:
            method (str,optional): Specifies the kind of interpolation as a string or as an 
            integer specifying the order of the spline interpolator to use. 
            The string has to be one of 'linear', 'nearest', 'nearest-up', 'zero', 'slinear', 
            'quadratic', 'cubic', 'quadratic' 
            and ‘cubic’ refer to a spline interpolation of zeroth, first, second or third order; 
            Default to ‘linear’.
            limit (int,optional): Maximum number of consecutive NaNs to fill. Must be greater than 0.
        Returns:
            ndarray: filtered array
        ''' 

        args = _get_args(locals())
        self._add2list(args = args, func_name='interpolate_na')

    def scaler(self,factor=1000):
        '''
        Scale the elements of the array by a defined factor

        Args:
            factor (float, optional): the scaling factor, Defaults to 1000.

        Returns:
            ndarray: filtered array
        ''' 
        args = _get_args(locals())
        self._add2list(args = args, func_name='rr_scaler')

    def butter_filter(self,cutoff, order = 4, btype = 'lowpass'):
        '''
        Apply a bandpass Butterworth filter to an array elements

        Args:
            fs (float, optional): Sampling frequency [Hz].
            cutoff (float): Cutoff frequency [Hz].
            order (int, optional): The order of the filter. Defaults to 4.
            btype ({‘lowpass’, ‘highpass’}, optional): filter type. Defaults to 'lowpass'.

        Returns:
            ndarray: filtered array
        ''' 
        args = _get_args(locals())
        self._add2list(args = args, func_name='butter_filter')
