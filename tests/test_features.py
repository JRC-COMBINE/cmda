# import sys, os, shutil
# import pytest
# import pandas as pd
# import numpy as np

# this_dir = os.path.dirname(os.path.abspath(__file__))

# if __name__ == "__main__":
#     sys.path.append(os.path.join(this_dir, ".."))
# from cmda.read_data import ReadCSV

# from cmda.data.wfdb import ecgrdvq_metadata
# from cmda.read_data import ReadWFDB
# from cmda.data import ecg_apb_sample


# def get_clean_temp_folder():
#     path = os.path.join(this_dir, "temp")
#     if os.path.exists(path):
#         shutil.rmtree(path)
#     os.mkdir(path)
#     return path

# if __name__ == "__main__":
#     pytest.main()

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