import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# from cmda.feature_engineering import FeatureExtraction
# from cmda.data_import._feature_extraction import extract_features

# x = [1,2,3,4,5,8]

# def fun1(x,y=4):
#     return np.min(x), np.std(x)

# labels = ('min','std')

# a = FeatureExtraction()
# a.add_feature.mean()
# a.add_feature.max()
# a.add_fun('udf',fun1,labels)
# a.apply_features(x,fs=1)

# print(a._features)
# print(a.features)


# data = pd.read_csv('/Users/pejman/Desktop/JRC/cmda/data/sample_signal.csv', index_col=0)
# print(data.shape)
# data = data.to_dict('list')

# a = extract_features(a,data)
# print(a)

# print(np.mean(data['II']))
# print(np.std(data['III']))


a = [1,2]
b = None
c = tuple(map(lambda e: (e, b), a))
print(c)
