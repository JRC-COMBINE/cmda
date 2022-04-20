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


    def rr_rm_outlier(self, low=0.2, high=2.5):

        args = _get_args(locals())
        self._add2list(args = args, func_name='rr_rm_outlier')

    def rr_rm_ectopic(self,k=2,thershold=0.3):

        args = _get_args(locals())
        self._add2list(args = args, func_name='rr_rm_ectopic')

    def rr_interpolate(self,method = 'linear', limit=4):

        args = _get_args(locals())
        self._add2list(args = args, func_name='rr_interpolate')

    def rr_scaler(self,factor=1000):

        args = _get_args(locals())
        self._add2list(args = args, func_name='rr_scaler')

    def butter_filter(self,cutoff, order = 4, btype = 'lowpass'):
        args = _get_args(locals())
        self._add2list(args = args, func_name='butter_filter')
