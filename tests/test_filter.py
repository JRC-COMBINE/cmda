import sys, os, shutil
import pytest
import pandas as pd
import numpy as np

this_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    sys.path.append(os.path.join(this_dir, ".."))
from cmda.data import ecg_apb_sample
from cmda.preprocessing import Filters
from cmda.data import ecg_apb_sample


def get_data():
    data = ecg_apb_sample()
    return data


def test_remove_outlier():
    data = get_data()["ECG"]
    lower, upper = [x + data.mean() / 2 for x in (data.min(), data.max())]

    filter = Filters()
    filter.add.rm_outlier(lower, upper)
    result = filter.transform(data)

    assert all((result >= lower) | np.isnan(result))
    assert all((result <= upper) | np.isnan(result))


def test_rm_outlier_quantile():
    data = get_data()["ECG"]
    filter = Filters()
    filter.add.rm_outlier_quantile(1, 0)
    result = filter.transform(data)
    assert all(result == data)

    filter = Filters()
    filter.add.rm_outlier_quantile(0.25, 0.75)
    result = filter.transform(data)
    lower, upper = np.quantile(data, (0.25, 0.75))
    assert all((result >= lower) | np.isnan(result))
    assert all((result <= upper) | np.isnan(result))


def test_interpolate_na():
    _data = get_data()["ECG"]
    index = len(_data) // 2
    data = _data.copy()
    data[index] = np.nan
    assert np.isnan(data[index])

    filter = Filters()
    filter.add.interpolate_na("linear")
    result = filter.transform(data)

    assert not np.isnan(result[index])
    assert result[index] == result[index - 1 : index + 2].mean()

    # Test Limit
    data[index - 1 : index + 3] = np.nan
    filter = Filters()
    filter.add.interpolate_na("linear", 1)
    result = filter.transform(data)
    assert not np.isnan(result[index - 1])
    assert all(np.isnan(x) for x in result[index : index + 2])


def test_scaler():
    data = get_data()["ECG"]
    factor = 1000
    filter = Filters()
    filter.add.scaler(factor)
    result = filter.transform(data.copy())
    assert all(result == data * factor)


def test_butter_filter():
    data = get_data()["ECG"]
    filter = Filters()
    filter.add.butter_filter(0.3)
    filter.transform(data)


def test_multiple_filters():
    data = get_data()["ECG"]
    l = len(data)
    state = np.random.RandomState(42)
    index = state.choice(range(l), size=int(l * 0.05), replace=False)
    for i in index:
        data[i] = np.nan
    assert all(np.isnan(data[i]) for i in index)

    filter = Filters()
    filter.add.rm_outlier_quantile(.9,.1)
    filter.add.interpolate_na()
    filter.add.scaler()    
    result = filter.transform(data.copy())
    
    assert all(not np.isnan(result[i]) for i in index)

if __name__=="__main__":
    test_multiple_filters()