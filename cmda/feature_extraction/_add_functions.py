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
        Add the "mean" function to the features instance.
        The feature object returns the average of the array elements..

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.mean()
            >>> feature.transform(x=x)
            {'mean': 1.27}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='mean')
        

    def max(self, nan_omit=True, min_samples=1):
        """
        Add the "max" function to the features instance.
        The feature object returns the maximum value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.max()
            >>> feature.transform(x=x)
            {'max': 7.0}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='max')


    def min(self, nan_omit=True, min_samples=1):
        """
        Add the "min" function to the features instance.
        The feature object returns the minimum value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.min()
            >>> feature.transform(x=x)
            {'min': -4.0}      
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='min')


    def std(self, nan_omit=True, min_samples=5):
        """
        Add the "std" function to the features instance.
        The feature object returns the standard deviation of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.std()
            >>> feature.transform(x=x)
            {'std': 2.56}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='std')


    def median(self, nan_omit=True, min_samples=5):
        """
        Add the "median" function to the features instance.
        The feature object returns the median value of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.median()
            >>> feature.transform(x=x)
            {'median': 1.0}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='median')


    def kurtosis(self, nan_omit=True, min_samples=5):
        """
        Add the "kurtosis" function to the features instance.
        The feature object returns the kurtosis of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.kurtosis()
            >>> feature.transform(x=x)
            {'kurtosis': 0.99}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='kurtosis')


    def skewness(self, nan_omit=True, min_samples=5):
        """
        Add the "skewness" function to the features instance.
        The feature object returns the skewness of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 5.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.skewness()
            >>> feature.transform(x=x)
            {'skewness': 0.18}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='skewness')

    def p2p(self, nan_omit=True, min_samples=1):
        """
        Add the "p2p" function to the features instance.
        The feature object returns the peak to peak value of the array elements.
        peak to peak (p2p) is the difference of the maxumum and minimum values of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.p2p()
            >>> feature.transform(x=x)
            {'p2p': 11.0}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='p2p')

    def rms(self, nan_omit=True, min_samples=5):
        """
        Add the "rms" function to the features instance.
        The feature object returns the root mean square of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.rms()
            >>> feature.transform(x=x)
            {'rms': 2.86}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='rms')

    def mad(self, nan_omit=True, min_samples=5):
        """
        Add the "rms" function to the features instance.
        The feature object returns the root mean square of the array elements.

        Args:
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.rms()
            >>> feature.transform(x=x)
            {'rms': 2.86}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='mad')

    def zcr(self, center=True,normalized = True, nan_omit=True, min_samples=1):
        """
        Add the "zcr" function to the features instance.
        The feature object returns the zero crossing rate of the array elements.

        Args:
            center (bool, optional): If True, center the array by its mean value, 
                which means the function returns the mean crossing rate of the array. Defaults to True.
            nan_omit (bool, optional): If True, the NaN values are omitted from the array. Defaults to True.
            min_samples (int, optional): Minimum number of non-NaN elements in the array required to run the function.
            If the number of non-NaN elements is less than this value, the feature object returns NaN. Defaults to 1.
        
        Description:
            The zero-crossing rate (ZCR) is the number of times a signal amplitude goes from positive to negative or negative to positive values. ZCR can be a measure of signal noisiness. ZCR of a centered signal determines the sign shift rate around its mean value. We can compute ZCR as follows:

            $$\frac{1}{2T}\displaystyle\sum_{t=2}^{T}|sgn(x_t)-sgn(x_t-1)|$$

            Where $T$ is the length of $x$, and $sgn$ is the sign function.

        Example:
            >>> from cmda.feature_extraction import Features
            >>> x = [1,2,-4,3,2,1,7,0,2,-1,1]
            >>> feature = Features()
            >>> feature.add.zcr(center=True)
            >>> feature.transform(x=x)
            {'zcr': 8}
        """
        args = _get_args(locals())
        self._add2list(args = args, func_name='zcr')


    def periodogram(self, window='boxcar', nfft=None, detrend='constant', scaling='density', log=False, band=None):
        '''
        Add the periodogram function to the features instance.
        
        The feature object returns the power spectral density estimate of the array using a periodogram.

        Args:
            window (str,optional): Desired window to use. See ```scipy.signal.get_window``` for a list of windows and required parameters. Defaults to ‘boxcar’.
            nfft (int,optional): Length of the FFT used. If None the length of the array will be used.
            detrend (str or False,optional): Specifies how to detrend each segment. If False, no detrending is done. Defaults to ‘constant’.
            scaling ({'density','spectrum'}, optional): Selects between computing the power spectral density (‘density’) where Pxx has units of V**2/Hz and computing the power spectrum (‘spectrum’) where Pxx has units of V**2, if x is measured in V and fs is measured in Hz. Defaults to ‘density’
            log (True or False, optional): If True, the function returns the log value of the power spectrum. Defaults to False.
            band (tuple, optional): Return the power spectrum in a desired specific frequency, Defaults to None.
        
        See also:
            ```scipy.signal.periodogram```
        '''        
        args = _get_args(locals())
        self._add2list(args = args, func_name='periodogram')


    def welch(self,window='hann', nperseg=None, noverlap=None, nfft=None, detrend='constant', scaling='density', average='mean', log=False, band=None):
        '''
        Add the periodogram welch function to the features instance.
        
        The feature object returns the power spectral density estimate of the array using welch method.

        Args:
            window (str,optional): Desired window to use. See ```scipy.signal.get_window``` for a list of windows and required parameters. Defaults to a Hann window..
            nperseg (int,optional): Length of each segment. Defaults to None, but if window is str or tuple, is set to 256, and if window is array_like, is set to the length of the window.
            noverlap (int,optional): Number of points to overlap between segments. If None, `noverlap = nperseg // 2`. Defaults to None.
            nfft (int,optional): Length of the FFT used. If None the length of the array will be used.
            detrend (str or False,optional): Specifies how to detrend each segment. If False, no detrending is done. Defaults to ‘constant’.
            scaling ({'density','spectrum'}, optional): Selects between computing the power spectral density (‘density’) where Pxx has units of V**2/Hz and computing the power spectrum (‘spectrum’) where Pxx has units of V**2, if x is measured in V and fs is measured in Hz. Defaults to ‘density’
            average ({'mean', 'median'}, optional): Method to use when averaging periodograms. Defaults to ‘mean’.
            log (True or False, optional): If True, the function returns the log value of the power spectrum. Defaults to False.
            band (tuple, optional): Return the power spectrum in a desired specific frequency, Defaults to None.
        
        Description:
            Welch’s method computes an estimate of the power spectral density by dividing the data into overlapping segments, computing a modified periodogram for each segment and averaging the periodograms.
        
        See also:
            ```scipy.signal.periodogram```

        Reference:
            P. Welch, “The use of the fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms”, IEEE Trans. Audio Electroacoust. vol. 15, pp. 70-73, 1967.
        ''' 
        args = _get_args(locals())
        self._add2list(args = args, func_name='welch')

    def energy(self,spectrum='ps',**kwargs):
        '''
        Add the energy function to the features instance.
        
        The feature object returns the energy (total power sum) of the array power spectrum.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
        
        Description:
            The power spectrum energy is the sum of the power spectrum, also known as the zero spectral moment ($SM_0$) \cite{sijin}. 
            It can be computed as follows:

            $$\displaystyle\sum_{j=1}^{j=M} P_j$$

            where $P_j$ is the power spectrum at the frequency bin j, and M is the length of frequency bin.

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        self._add2list(args = args, func_name='energy')

    def mnf(self,spectrum='ps',**kwargs):
        '''
        Add the ```cmda.spectral_frequency.mnf``` function to the features instance.
        
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

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        Add the median frequency function to the features instance.
        
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

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        Add ```cmda.spectral_features.stdf``` function to the features instance.
        
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

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        Add `vcf` function to the features instance.
        
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

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        Add the `psr` function to the features instance.
        
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

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        Add the spectral peaks function to the features instance.
        
        The feature object returns the *n* first peaks of the power spectrum of an array.

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

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.        

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
        Add band energy function to the features instance.
        
        The feature object returns the energy of a power spectral density in a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.
            normalize (bool, optional): if True, normalize by the spectrum total energy. Defaults to True.
        
        Description:
            Band power is the power spectral density in a specified frequency band. 

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.
        
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
        Add ```cmda.spectral_features.band_std``` function to the features instance.
        
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
        Add the mean frequncy band function to the features instance.
        
        The feature object returns the mean frequency of a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.

        Description:
            The mean frequency (MNF) of a spectrum is the center of the distribution of power across a specified frequency band. 

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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
        Add median freuqncy band function to the features instance.
        
        The feature object returns the median frequency of a specified frequency band.

        Args:
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.
            low (float, optional): low frequency band. if None, the minimum frequency is selected. Defaults to None.
            high (float, optional): high frequency band. if None, the maximum frequency is selected. Defaults to None.
        
        Description:
            The median frequency is the frequency at which the power spectrum in a specified frequency band
            is divided into two parts with equal powers

        Reference:
            Phinyomark, A., Thongpanja, S., Hu, H., Phukpattaranont, P. & Limsakul, C. The Usefulness of Mean and Median Frequencies in Electromyography Analysis. in Computational Intelligence in Electromyography Analysis - A Perspective on Current Applications and Future Challenges (ed. Naik, G. R.) (InTech, 2012). doi:10.5772/50639.

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

    def band_agg(self,spectrum='ps',low = None ,high = None, **kwargs):
        '''
        Add an aggregate of spectral functions to the features instance.
        
        The feature object returns the following features of a specified frequency band:
        + total power
        + mnf
        + vcf
        + spectral entropy
        + frequency of the power spectrum maximum

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
            {'power_[100,500]Hz': 4.60e-05,
            'mnf_[100,500]Hz': 182.63,
            'vcf_[100,500]Hz': 9422.89,
            'peak_[100,500]Hz': 100.0,
            'entropy_[100,500]Hz': 0.91}}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='band_agg')

    def spectral_entropy(self,normalized=True,spectrum='ps',**kwargs):
        '''
        Add `spectral_entropy` function to the features instance.
        
        The feature object returns the spectral entropy of the array elements.

        Args:
            normalized (True or False,optional): if True, the entropy is normlized by the `log2` of the array length. Defaults to True.
            spectrum ({'ps','welch'}, optional): method to calculate the power spectrum. Defaults to 'ps'.

        Description:
            Spectral entropy, based on the Shannon entropy, is a measure of the randomness
            of a power spectrum frequency distribution. 

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.perm_entropy(m=2,tau=1)
            >>> feature_obj.transform(x=x)
            {'perm_entropy_m2_t1': 4.80}
        '''        
        args = _get_args(locals())
        self._add2list(args = args, func_name='spectral_entropy')

    def perm_entropy(self,m=3,tau=1):
        '''
        Add "permutation_entropy" function to the features instance.
        
        The feature object returns the permutation entropy of the array elements.

        Args:
            m (int): embedding space dimesnion. Defaults to 2.
            tau (int): embedding space delay. Defaults to 1.

        Description:
            Permutation entropy is another derivation of Shannon entropy, 
            used to assess the complexity of time series data.
            It quantifies the complexity of a system based on similar ordinal patterns.

        Reference:
            Bandt, C. & Pompe, B. Permutation Entropy: A Natural Complexity Measure for Time Series. Phys. Rev. Lett. 88, 174102 (2002).

        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature_obj = Features()
            >>> feature_obj.add.perm_entropy(m=2,tau=1)
            >>> feature_obj.transform(x=x)
            {'perm_entropy_m2_t1': 4.80}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='perm_entropy')

    def sample_entropy(self,m=2,std_ratio=0.2,down_ratio=0):
        '''
        Add "sample_entropy" function to the features instance.
        
        The feature object returns the sample entropy of the array elements.

        Args:
            m (int): embedding space dimesnion. Defaults to 2.
            std_ratio (float): ratio of the distance thershold to the standard devitaion of the data. Defaults to 0.2.
            down_ratio (float, optional): In the case of very large array, the data can be downsampled 
                with this ratio factor to save computation time. If set to zero, the original data is used.
                Defaults to 0.

        Description:
            Sample entropy, a derivation of Shannon entropy, 
            is a method for estimating the irregularity of time series data.
        
        Reference:
            Richman, J. S. & Moorman, J. R. Physiological time-series analysis using approximate entropy and sample entropy. American Journal of Physiology-Heart and Circulatory Physiology 278, H2039–H2049 (2000).

        
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature = Features()
            >>> feature.add.sample_entropy(m=2, tau=1)
            >>> feature.transform(x=x)
            {'sample_entropy_m2': 0.86}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='sample_entropy')

    def swt_features(self,features,wavelet='db5', level=5, start_level = 0,**kwargs):
        '''
        Add "swt_features" function to the features instance.
        
        The feature object returns the given `features` as input from the SWT coefficients of the array elements.

        Args:
            features (list): List of desired features which can be selected from: ['mean','std','kurt','skew','p2p','rms','mnf','mdf','peak_freq']
            wavelet (str): Wavelet to use. See ```pywt.families``` for a list of wavelets. Defaults to 'db5'
            level (int): The number of decomposition steps to perform. Defaults to 5. 
            start_level (int,optional): Return the features from the `start_level`. Defaults to 0.

        Description:
            Stationary Wavelet Transform (SWT), also known as Undecimated wavelet transform, is a translation-invariance modification of the Discrete Wavelet Transform that does not decimate coefficients at every transformation level.
        
        Reference:
            DB Percival and AT Walden. Wavelet Methods for Time Series Analysis. Cambridge University Press, 2000.
        
        See also:
            [```pywt.swt```](https://pywavelets.readthedocs.io/en/latest/ref/swt-stationary-wavelet-transform.html)
        Example:
            >>> import numpy as np
            >>> from cmda.feature_extraction import Features
            >>> t = np.arange(5000)
            >>> x = np.sin(0.03*t) + np.cos(0.3*t+4)
            >>> feature = Features()
            >>> feature.add.swt_features(features=['mean','rms','mnf','peak_freq'], level=6, start_level=2)
            >>> feature.transform(x=x)
            {'swt_cA_6_mean': 0.0036450929063020455,
            'swt_cA_6_rms': 0.697382052281463,
            'swt_cA_6_mnf': 4.801953817115636,
            'swt_cA_6_peak_freq': 4.807692307692308,
            'swt_cD_6_mean': 1.7792035651044174e-18,
            'swt_cD_6_rms': 0.12435558035702293,
            'swt_cD_6_mnf': 7.495235273855551,
            'swt_cD_6_peak_freq': 4.807692307692308,
            'swt_cD_5_mean': 8.896017825522087e-19,
            'swt_cD_5_rms': 0.03755044254533484,
            'swt_cD_5_mnf': 33.89157204953992,
            'swt_cD_5_peak_freq': 47.67628205128205,
            'swt_cD_4_mean': 6.227212477865461e-19,
            'swt_cD_4_rms': 0.6604946723912127,
            'swt_cD_4_mnf': 47.701920399254455,
            'swt_cD_4_peak_freq': 47.67628205128205,
            'swt_cD_3_mean': 4.0032080214849397e-19,
            'swt_cD_3_rms': 0.24854516466019605,
            'swt_cD_3_mnf': 47.903198358173064,
            'swt_cD_3_peak_freq': 47.67628205128205,
            'swt_cD_2_mean': -6.560813146322539e-19,
            'swt_cD_2_rms': 0.017198230129006772,
            'swt_cD_2_mnf': 68.94286686752932,
            'swt_cD_2_peak_freq': 47.67628205128205}
        '''
        args = _get_args(locals())
        self._add2list(args = args, func_name='swt_features')

    def hrv_time_domain_features(self, nan_lim_ratio=0.1):
        args = _get_args(locals())
        self._add2list(args = args, func_name='hrv_time_domain_features')

    def hrv_spectral_features(self,fs, method="cubic"):
        args = _get_args(locals())
        self._add2list(args = args, func_name='hrv_spectral_features')

    def hrv_nonlinear_features(self):
        args = _get_args(locals())
        self._add2list(args = args, func_name='hrv_nonlinear_features')






