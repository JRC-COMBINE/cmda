# import numpy as np
# import pandas as pd

# import matplotlib.pyplot as plt
# from itertools import zip_longest
# import inspect

# from statsmodels.tsa.stattools import acf

# from cmda.feature_engineering.feature_object import Features

# # from cmda.feature_engineering import FeatureExtraction
# # from cmda.data_import._feature_extraction import extract_features

# # x = [1,2,3,4,5,8,np.nan]

# def fun1(x,y=4):
#     return np.min(x), np.std(x)

# labels = ('min','std')

# a = Features()
# a.add_feature.mean(nan_omit=False)
# a.add_feature.max()
# a.add_feature.mean_freq(spectrum='welch',nperseg=512)
# a.add_feature.mean()
# a.add_feature.mean(min_samples=10000000)
# a.add('udf',fun1,labels)


# print(a._features)
# print(a.features)


# data = pd.read_csv('/Users/pejman/Desktop/JRC/cmda/data/sample_signal.csv', index_col=0)
# # print(data.shape)
# data = data.to_dict('list')
# x = data['II']

# # a = extract_features(a,data)
# # print(a)

# # print(np.mean(data['II']))
# # print(np.std(data['III']))

# a.transform(x=x, fs=1)
# print(a._features)
# print(a.features)


# tutorial 1
from cmda.feature_extraction import Features
from cmda.data import ecg_apb_sample

data = ecg_apb_sample()
x = data["ECG"]

feature = Features()

# add frequency-domain built-in features
feature.add.mnf(spectrum="ps")
feature.add.mdf(spectrum="ps")
feature.add.stdf(spectrum="ps")
feature.add.psr(spectrum="welch", int_limit_ratio=0.01)
feature.add.peaks(spectrum="welch", n_peaks=1, height=True, width=True)
feature.add.band_sum(spectrum="ps", low=1, high=7)
feature.add.band_mnf(spectrum="ps", low=1, high=7)

res = feature.transform(x=x, fs=125)
print(res)
