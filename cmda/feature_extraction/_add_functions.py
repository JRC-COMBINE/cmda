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

        while func_name_ in self._ListOfFunctions:
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
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
            >>> fs = 1
            >>> feature = Features()
            >>> feature.add.mean()
            >>> feature.transform(x=x,fs=fs)
            {'mean': 5.5}
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
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
            >>> fs = 1
            >>> feature = Features()
            >>> feature.add.max()
            >>> feature.transform(x=x,fs=fs)
            {'max': 10}
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
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
            >>> fs = 1
            >>> feature = Features()
            >>> feature.add.min()
            >>> feature.transform(x=x,fs=fs)
            {'min': 1}        
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
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
            >>> fs = 1
            >>> feature = Features()
            >>> feature.add.std()
            >>> feature.transform(x=x,fs=fs)
            {'std': 2.87228}
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
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
            >>> fs = 1
            >>> feature = Features()
            >>> feature.add.median()
            >>> feature.transform(x=x,fs=fs)
            {'median': 5.5}
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
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> x = np.array([1,2,3,4,5,6,7,8,9,10])
            >>> fs = 1
            >>> feature = Features()
            >>> feature.add.kurtosis()
            >>> feature.transform(x=x,fs=fs)
            {'kurtosis': -1.224}
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


    def periodogram(self,band=None, window='boxcar', nfft=None, detrend='constant', scaling='density', log=False):
        args = _get_args(locals())
        self._add2list(args = args, func_name='periodogram')


    def welch(self,band=None, window='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', scaling='density', average='mean', log=False):
        args = _get_args(locals())
        self._add2list(args = args, func_name='welch')

    def mnf(self,spectrum='ps',**kwargs):
        '''
        Add the ```cmda.spectral_frequency.mnf``` function to the features.
        
        The feature object returns the mean frequency of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
        
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
        Add the ```cmda.spectral_features.mdf``` function to the features.
        
        The feature object returns the median frequency of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
        
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
        '''
        Add ```cmda.spectral_features.stdf``` function to the features.
        
        The feature object returns the standard deviation of central frequency of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
        
        Description:
            Standard deviation of central frequency (STDF) can be defined as 
            the standard deviation of power spectrum amplitudes from its mean frequency:

            $$\sqrt{\frac{\displaystyle\sum_{j=1}^{M} P_j(f_j-MNF)^2}{\displaystyle\sum_{j=1}^{M} P_j}}$$

            where $MNF$ is the mean frequency of the power spectrum, 
            $f_j$ is the frequency value of the power spectrum at the frequency bin $j$, 
            $P_j$ is the power spectrum at the frequency bin j, 
            and M is the length of frequency bin.

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.stdf(spectrum="ps")
            >>> feature_obj.transform(x=x,fs=fs)
            {'stdf': 21.25}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='stdf')

    def vcf(self,spectrum='ps',**kwargs):
        '''
        Add ```cmda.spectral_features.vcf``` function to the features.
        
        The feature object returns the variance of central frequency of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
        
        Description:
            Variance of central frequency (VCF) can be defined as 
            the variance of power spectrum amplitudes from its mean frequency:

            $$\frac{\displaystyle\sum_{j=1}^{M} P_j(f_j-MNF)^2}{\displaystyle\sum_{j=1}^{M} P_j}$$

            where $MNF$ is the mean frequency of the power spectrum, 
            $f_j$ is the frequency value of the power spectrum at the frequency bin $j$, 
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
            {'vcf': 463.34}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='vcf')

    def psr(self,spectrum='ps',int_limit_ratio = 0.01,**kwargs):
        '''
        Add ```cmda.spectral_features.psr``` function to the features.
        
        The feature object returns the power spectral ratio of the array.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            int_limit_ratio (float, optional): integral limit as a ratio of the whole frequecy range. Defaults to 0.01.      

        Description:
            Power spectrum ratio (PSR) is a ratio between the energy around 
            the maximum value of the power spectrum and the whole energy of 
            the power spectrum. It can be computed as follows:

            $$\frac{\displaystyle\sum_{j={f_0}-n}^{j={f_0}+n} P_j}{\displaystyle\sum_{j=1}^{M} P_j}$$

            where $f_0$ is the peak frequency, 
            $n$ is the integral limit, 
            $P_j$ is the power spectrum at the frequency bin j, 
            and M is the length of frequency bin.

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.psr(spectrum="ps", int_limit_ratio=0.01)
            >>> feature_obj.transform(x=x,fs=fs)
            {'psr': 0.50}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='psr')

    def peaks(self,spectrum='ps',n_peaks =1, height = True, width = True,**kwargs):
        '''
        Add ```cmda.spectral_features.peaks``` function to the features.
        
        The feature object returns the *n* first peaks of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            n_peaks (int, optional): number of peaks. Defaults to 1.
            height (bool, optional): if True, returns the height of the peaks. Defaults to True.
            width (bool, optional): if True, returns the width of the peaks. Defaults to True.
        
        Description:
            Peak frequency is a frequency at which the maximum of power spectrum occurs:

            $$\argmax(P_j) , j=1,...,M$$

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
            >>> feature_obj.add.peaks(spectrum="ps", n_peaks=1, height=True, width=True)
            >>> feature_obj.transform(x=x,fs=fs)
            {'peak_freq_1': 4.80, 'peak_height_1': 2.37, 'peak_width_1': 1.017}
        '''        
        args = _get_args(locals())
        self._add2list(args = args, func_name='peaks')

    def band_power(self,spectrum='ps',low = None ,high = None, normalize = True, **kwargs):
        '''
        Add ```cmda.spectral_features.band_power``` function to the features.
        
        The feature object returns the power spectral density in a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.
            normalize (bool, optional): if True, normalize by the spectrum total energy. Defaults to True.
        
        Description:
            Band power is the power spectral density in a specified frequency band. 
            It can be computed as follows:

            $$\displaystyle\sum_{j=f_low}^{j=f_high} P_j$$

            if normalize by the total power density:

            $$\frac{\displaystyle\sum_{j=f_low}^{j=f_high} P_j}{\displaystyle\sum_{j=1}^{M} P_j}$$

            where $f_low$ and $f_high$ are the low and high frequency band, 
            $P_j$ is the power spectrum at the frequency bin j, 
            and M is the length of frequency bin.
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.band_power(spectrum="ps", low=2, high=15, normalize=True)
            >>> feature_obj.transform(x=x,fs=fs)
            {'band_power': 0.50}
        '''        
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_power')

    def band_std(self,spectrum='ps',low = None ,high = None, normalize = True, **kwargs):
        '''
        Add ```cmda.spectral_features.band_std``` function to the features.
        
        The feature object returns the power spectral standard deviation in a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.
            normalize (bool, optional): if True, normalize by the power spectral density average. Defaults to True.
        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.band_std(spectrum="ps", low=2, high=15, normalize=True)
            >>> feature_obj.transform(x=x,fs=fs)
            {'band_std': 117.55}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_std')

    def band_mnf(self,spectrum='ps',low = None ,high = None, **kwargs):
        '''
        Add ```cmda.spectral_features.band_mnf``` function to the features.
        
        The feature object returns the mean frequency of a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.band_mnf(spectrum="ps", low=2, high=15, normalize=True)
            >>> feature_obj.transform(x=x,fs=fs)
            {'band_mnf': 4.81}
        '''
        
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_mnf')

    def band_mdf(self,spectrum='ps',low = None ,high = None, **kwargs):
        '''
        Add ```cmda.spectral_features.band_mnf``` function to the features.
        
        The feature object returns the median frequency of a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> fs = 1000
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.band_mdf(spectrum="ps", low=2, high=15, normalize=True)
            >>> feature_obj.transform(x=x,fs=fs)
            {'band_mdf': 4.80}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_mdf')


    def swt_features(self,features,wavelet, level, start_level = 1,**kwargs):
        args = _get_args(locals())
        self._add2list(args = args, func_name='swt_features')








