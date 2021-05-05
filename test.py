import numpy as np

from cmda.feature_engineering import FeatureExtraction

x = [1,2,3,4,5,6]

def fun1(x,y=4):
    return np.min(x), np.std(x)

labels = ('min','std')

a = FeatureExtraction(x)
a.add_feature.mean()
a.add_feature.max()
a.add_fun('udf',fun1,labels)
a.apply_features()

print(a._features)
print(a.features)