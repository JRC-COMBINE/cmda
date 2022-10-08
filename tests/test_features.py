#%%
import sys, os
import numpy as np

this_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    sys.path.append(os.path.join(this_dir, ".."))
from cmda.data import ecg_apb_sample
from cmda.preprocessing import Filters
from cmda.data import ecg_apb_sample
from cmda.feature_extraction import Features
from cmda.feature_extraction import extract_features
from cmda.data import ecg_apb_sample

def get_data():
    data = ecg_apb_sample()
    return data
#%%
def test_time_domain_features():
    data = get_data()
    d = data['ECG']
    # Create the feeature object
    features = Features()

    # Add built-in features

    features.add.mean()
    features.add.max()
    features.add.min()
    features.add.median()
    features.add.std()
    features.add.skewness()
    features.add.kurtosis()
    features.add.p2p()
    features.add.rms()
    features.add.zcr()
    features.add.mad()
    # extract eatures
    res = extract_features(data=data, feature_obj=features)
    assert "ECG_mean" in res
    assert np.allclose(d.mean(),res["ECG_mean"])

    assert "ECG_max" in res
    assert np.allclose(d.max(), res["ECG_max"])

    assert "ECG_min" in res
    assert np.allclose(d.min(), res["ECG_min"])

    assert "ECG_median" in res
    assert np.allclose(np.median(d), res["ECG_median"])

    assert "ECG_std" in res
    assert np.allclose(d.std(), res["ECG_std"])

    from  scipy.stats import skew, kurtosis

    assert "ECG_skewness" in res
    assert np.allclose(skew(d), res["ECG_skewness"])

    assert "ECG_kurtosis" in res
    assert np.allclose(kurtosis(d), res["ECG_kurtosis"])

    assert "ECG_p2p" in res
    assert np.allclose(np.ptp(d), res["ECG_p2p"])

    assert "ECG_rms" in res
    assert np.allclose(np.sqrt(np.mean(d**2)), res["ECG_rms"])

    assert "ECG_zcr" in res
    assert np.allclose(0.08246597277822258,res["ECG_zcr"])

    assert "ECG_mad" in res
    mad = np.median(np.abs(d-np.median(d)))
    assert np.allclose(mad,res["ECG_mad"])



if __name__=="__main__":
    test_time_domain_features()

# %%
