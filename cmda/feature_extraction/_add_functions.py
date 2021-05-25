import numpy as np



def _get_args(args):
    args.pop('self')
    if 'kwargs' in args.keys():
        kwargs = args.pop('kwargs')
        args = {**args,**kwargs}
    return args


class _AddFeatures:
    def __init__(self):
        self._ListOfFunctions = {}

    def _add2list(self,args,func_name):
        func_name_ = func_name+"__0"

        while func_name in self._ListOfFunctions:
            func_name_splited = func_name_.split('__')
            new_func_name = int(func_name_splited[1])+1
            func_name_ = f'{func_name}__{str(new_func_name)}'

        self._ListOfFunctions[func_name_] = args


    def mean(self, nan_omit=True, min_samples=1):
        """
        Add the "mean" function to the features.
        The feature object returns the average of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='mean')
        

    def max(self, nan_omit=True, min_samples=1):
        """
        Add the "max" function to the features.
        The feature object returns the maximum value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='max')


    def min(self, nan_omit=True, min_samples=1):
        """
        Add the "min" function to the features.
        The feature object returns the minimum value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='min')


    def std(self, nan_omit=True, min_samples=5):
        """
        Add the "std" function to the features.
        The feature object returns the standard deviation of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='std')


    def median(self, nan_omit=True, min_samples=5):
        """
        Add the "median" function to the features.
        The feature object returns the median value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='median')


    def kurtosis(self, nan_omit=True, min_samples=5):
        """
        Add the "kurtosis" function to the features.
        The feature object returns the kurtosis of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='kurtosis')


    def skewness(self, nan_omit=True, min_samples=5):
        """
        Add the "skewness" function to the features.
        The feature object returns the skewness of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='skewness')

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
        args = _get_args(locals())
        self._add2list(args = args, func_name='p2p')

    def rms(self, nan_omit=True, min_samples=5):
        """
        Add the "rms" function to the features.
        The feature object returns the root mean square of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='rms')

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
        args = _get_args(locals())
        self._add2list(args = args, func_name='zcr')


    def mnf(self,spectrum='ps',**kwargs):
        '''
        Add the *mnf* function to the features.
        
        The feature object returns the mean frequency of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectum. Defaults to 'ps'.
        
        Description:
            Mean frequency (MNF) of a spectrum is the center of the distribution of power across frequencies. 
            It is calculated as the sum of product of the power spectrum and the frequency divided by the total sum of the power spectrum.
            The difintion is as follows:

            $$\frac{\displaystyle\sum_{j=1}^{M} f_j P_j}{\displaystyle\sum_{j=1}^{M} P_j}$$

            where $f_j$ is the frequency value of the power spectrum at the frequency bin $j$, 
            $P_j$ is the power spectrum at the frequency bin j, 
            and M is the length of frequency bin.

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.mnf(spectrum="ps")
            >>> feature_obj.transform(x=x,fs=fs)
            {'mnf': 26.263}
        '''        
        args = _get_args(locals())
        self._add2list(args = args, func_name='mnf')

    def mdf(self,spectrum='ps',**kwargs):
        '''
        Add the *mdf* function to the features.
        
        The feature object returns the median frequency of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectum. Defaults to 'ps'.
        
        Description:
            Median frequency (MDF) is a frequency at which the power spectrum is divided into 
            two parts with equal powers:

            $$\displaystyle\sum_{j=1}^{MDF} P_j = \displaystyle\sum_{j=MDF}^{M} P_j$$

            where $MDF$ is the median frequency, 
            $P_j$ is the power spectrum at the frequency bin j, 
            and M is the length of frequency bin.

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.mdf(spectrum="ps")
            >>> feature_obj.transform(x=x,fs=fs)
            {'mdf': 8.20}
        '''  
        args = _get_args(locals())
        self._add2list(args = args, func_name='mdf')

    def stdf(self,spectrum='ps',**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='stdf')

    def vcf(self,spectrum='ps',**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='vcf')

    def psr(self,spectrum='ps',int_limit_ratio = 0.01,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='psr')

    def peaks(self,spectrum='ps',n_peaks =1, height = True, width = True,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='peaks')

    def band_sum(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_sum')

    def band_std(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_std')

    def band_mnf(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_mnf')

    def band_mdf(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_mdf')

    def band_stdf(self,spectrum='ps',low = None ,high = None, normalize = True, log = False,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_stdf')






