import os

import numpy as np 
import pandas as pd 





def ecg_apb_sample():
    _path = os.path.dirname(__file__)
    data_path = os.path.join(_path,'ecg_abp_sample.csv')

    df = pd.read_csv(data_path, index_col=0)

    data = {}
    data['ECG'] = np.array(df['ECG'])
    data['ABP'] = np.array(df['ABP'])

    return data


