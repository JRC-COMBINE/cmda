from cmda.feature_extraction import Features
from cmda.data import ecg_apb_sample

data = ecg_apb_sample()
x = data["ECG"]


feature = Features()

# add time-domain built-in features
feature.add.mean()
feature.add.max()
feature.add.min()
feature.add.median()
feature.add.skewness()
feature.add.kurtosis()
feature.add.std()
feature.add.p2p()
feature.add.zcr(center=True)

res = feature.transform(x=x, fs=125)
print(res)
