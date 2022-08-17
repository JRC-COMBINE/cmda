import sys, os, shutil
import pytest
import pandas as pd
import numpy as np

this_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    sys.path.append(os.path.join(this_dir, ".."))
from cmda.read_data import ReadCSV

from cmda.data.wfdb import ecgrdvq_metadata
from cmda.read_data import ReadWFDB
from cmda.data import ecg_apb_sample


def get_clean_temp_folder():
    path = os.path.join(this_dir, "temp")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    return path


def test_sample_data():
    data = ecg_apb_sample()
    assert type(data) == dict
    assert len(data) == 2
    assert "ECG" in data
    assert "ABP" in data
    ecg = data["ECG"]
    abp = data["ABP"]
    assert len(ecg) == 1250
    assert len(abp) == 1250
    assert ecg.mean() == -0.02365354330708655
    assert abp.mean() == 72.385
    assert ecg.std() == 0.09125083485333008
    assert abp.std() == 13.268216310510619


def generate_csv_for_input():
    path = get_clean_temp_folder()
    x = np.arange(2000)
    A = x / 2
    B = np.sin(x)
    x = np.arange(1300)
    C = 3 * x + 4
    D = np.sin(x * 1.5) * 1.5
    df1 = pd.DataFrame({"A": A, "B": B})
    df2 = pd.DataFrame({"C": C, "D": D})
    df_names = {"df1": ["A", "B"], "df2": ["C", "D"]}
    p1 = os.path.join(path, "df1.csv")
    p2 = os.path.join(path, "df2.csv")
    df1.to_csv(p1)
    df2.to_csv(p2)
    paths = [p1, p2]
    for path in paths:
        assert os.path.exists(path)
    return paths, df_names


def test_ReadCSV():
    files, df_names = generate_csv_for_input()
    importer = ReadCSV(files)
    data = importer.load()
    assert len(data) == len(df_names)
    for element, (name, columns) in zip(data, df_names.items()):
        assert element["fs"] == 1
        assert name in element

        df = element[name]
        assert len(df) == len(columns) + 1  # + Index Col
        for col in columns:
            assert col in columns
test_ReadCSV()

def test_ReadWFDB():
    # Load the meta-data
    metadata = ecgrdvq_metadata()

    n = 5
    # get the record names and their corresponding public directories
    record_names = metadata["record_name"][:n]
    public_dir = metadata["public_dir"][:n]

    # Build the importer object using ReadWFDB
    # Set the channels to ["II",'V1'] to import these channels exclusively.
    importer = ReadWFDB(record_names=record_names, pn_dir=public_dir, channels=["II", "V1"])
    data = importer.load()
    assert len(data) == n
    for record, record_name in zip(data, record_names):
        assert record["fs"] == 1000
        assert record_name in record
        r = record[record_name]
        assert len(r) == 2
        assert "II" in r
        assert "V1" in r
        assert len(r["II"]) == 10000
        assert len(r["V1"]) == 10000


if __name__ == "__main__":
    pytest.main()
# from cmda import data as d
# from cmda.data import ReadCSV

# from cmda.data import ecg_apb_sample

# def test_sample_data():
#     data = ecg_apb_sample()
#     assert type(data) == dict
#     assert len(data) == 2
#     assert "ECG" in data
#     assert "ABP" in data


# # def test_csv

# from cmda.feature_extraction import Features
# from cmda.feature_extraction import extract_features
# from cmda.data import ecg_apb_sample

# # load the data
# data = ecg_apb_sample()

# # Create the feeature object
# features = Features()

# # Add built-in features
# features.add.std()
# features.add.mnf()
# features.add.stdf()

# # extract eatures
# res = extract_features(data=data, feature_obj=features)


# from cmda.feature_extraction import Features
# from cmda.feature_extraction import extract_features
# from cmda.data import ecg_apb_sample

# # load the data
# data = ecg_apb_sample()

# # Create the feature object for ECG signal
# ecg_features = Features()

# # Add built-in features
# ecg_features.add.mnf()
# ecg_features.add.stdf()


# # Create the feature object for ECG signal
# abp_features = Features()

# # Add built-in features
# abp_features.add.mean()
# abp_features.add.std()
# abp_features.add.max()
# abp_features.add.min()

# # Create the feature object as a dict
# features = {'ECG':ecg_features, 'ABP':abp_features}

# # extract eatures
# res = extract_features(data=data, feature_obj=features)

# res
