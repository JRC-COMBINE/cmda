import numpy as np 


from cmda.feature_extraction import Features
from cmda.data import ecg_apb_sample

data = ecg_apb_sample()

x = data['ECG']

print(x)


feature_obj = Features()

feature_obj.add.swt_features(wavelet='db5',features = ['mean','var','skew'],level=5, start_level=2)

res = feature_obj.transform(x,fs=125)

print(res)