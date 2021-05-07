import numpy as np
import pandas as pd

import concurrent.futures
from functools import partial
from tqdm import tqdm




class Pipeline:

    def __init__(self,importer,features, filters = None, n_jobs=-1):
        self.importer = importer
        self.features = features
        self.filters = filters

    def run(self,rec_path_list,pb_dir):

        if not isinstance(pb_dir,list):
            path = tuple(map(lambda x: (x, pb_dir), rec_path_list))
        else:
            path = zip(rec_path_list,pb_dir)

        res = []
        for p in path:
            res.append(_pipeline(importer=self.importer, features=self.features, path = p))

        return res


    def run_p(self,rec_path_list,pb_dir):

        if not isinstance(pb_dir,list):
            path = tuple(map(lambda x: (x, pb_dir), rec_path_list))
        else:
            path = zip(rec_path_list,pb_dir)

        pip_func = partial(_pipeline, importer = self.importer, features = self.features)

        path_progress = tqdm(path)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            res = executor.map(pip_func, path_progress)

        res = list(res)
        return res



def _pipeline(path,importer, features):
    rec_path = path[0]
    pb_dir = path[1]
    data = importer._get_data(rec_path = rec_path, pb_dir=pb_dir)

    keys = list(data.keys())
    rec_name = keys[0]
    fs = data['fs']
    data = data[rec_name]
     
    res = features._get_features(data = data, fs=fs)
    res = {rec_name:res}

    return res







def extract_features(feature_obj, data: dict, fs: int = 1) -> dict:
    """
    Extarct features from a dictionary containing multiple arrays.

    Args:
        feature_obj (python_object): Feature object
        data (dict): Dictionary containing multiple arrays
        fs (int, optional): Sampling frequency of the arrays. Defaults to 1.

    Returns:
        dict: Extracted features
    """
    res = {}
    for key, x in data.items():
        feature_obj.apply_features(x = x, fs = fs)
        res_key = feature_obj.features
        res_key = {f'{key}_{k}': v for k, v in res_key.items()}
        res = {**res,**res_key}

    return res


def extract_features_dataframe(feature_obj, df: pd.DataFrame, fs: int = 1) -> dict:
    '''
    Extarct features from columns of a dataframe.

    Args:
        feature_obj (python_object): Feature object
        df (pd.DataFrame): Dataframe, where each column represents an array
        fs (int, optional): Sampling frequency of the arrays. Defaults to 1.

    Returns:
        dict: [description]
    '''

    data = df.to_dict('list')
    res = extract_features(
        feature_obj=feature_obj,
        data=data,
        fs=fs
    )

    return res



class FeatureExtraction:

    def __init__(self,feature_obj):
        self.feature_obj = feature_obj

    def _get_features(self,data,fs):
        res = extract_features(data=data, feature_obj=self.feature_obj, fs=fs)
        return res