

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


class _AddFilters:
    def __init__(self):
        self._ListOfFunctions = {}

    @add2list
    def butter_filter(self, cutoff, order = 4, btype = 'lowpass'):

        return _get_args(locals())


    @add2list
    def rm_outlier_quantile(self, q_up = 1, q_low = 0):

        return _get_args(locals())