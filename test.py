import numpy as np 


from cmda.feature_extraction import Features
from cmda.data import ecg_apb_sample

data = ecg_apb_sample()

x = data['ECG']

print(x)


feature_obj = Features()

feature_obj.add.mnf()
feature_obj.add.band_power(low=1,high=10)
feature_obj.add.band_power(low=10,high=20)

res = feature_obj.transform(x,fs=125)

print(res)