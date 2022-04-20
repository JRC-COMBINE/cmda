import os

import numpy as np 
import pandas as pd
from wfdb import rdrecord
from .wfdb import ecgrdvq_metadata





def ecg_apb_sample():
    _path = os.path.dirname(__file__)
    data_path = os.path.join(_path,'ecg_abp_sample.csv')

    df = pd.read_csv(data_path, index_col=0)

    data = {}
    data['ECG'] = np.array(df['ECG'])
    data['ABP'] = np.array(df['ABP'])

    return data


def get_csv_samples(path):
    metadata = ecgrdvq_metadata()

    record_names = metadata['record_name'][0:8]
    public_dir = metadata['public_dir'][0:8]
    
    print('Downloading the sample CSV files ...')
    for rec,pb in zip(record_names,public_dir):
        record = rdrecord(record_name=rec, pn_dir=pb, channel_names=['II','V1','AVF'])
        data = record.p_signal
        data = pd.DataFrame(data)
        data.columns = ['II','V1','AVF']
        data.to_csv(os.path.join(path,f'{rec}.csv'))
        
    print("finished!")

