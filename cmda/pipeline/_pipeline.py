import numpy as np
import pandas as pd

from functools import partial
from tqdm import tqdm
from pathos.multiprocessing import ProcessingPool as Pool


from ..feature_extraction.feature_extraction import _extract_features
from ..preprocessing.filter_object import apply_filters





class Pipeline:

    def __init__(self,importer,features, filters = None, n_jobs=1):
        self.importer = importer
        self.features = features
        self.filters = filters


    def run(self, n_jobs = 1, dataframe_output = False):

        iterator = self.importer.iterator

        pip_func = partial(_pipeline, importer = self.importer, features = self.features, filters = self.filters)

        print(f"Running the pipeline on {len(iterator)} instances...\n")
        if n_jobs == 1:
            iterator_progress = tqdm(iterator)
            res = map(pip_func, iterator_progress)
        else:
            p = Pool()
            res = tqdm(p.map(pip_func, iterator),total=len(iterator))


        res = {i[0]:i[1] for i in res if i is not None}

        if dataframe_output:
            res = pd.DataFrame(res).T

        print("finished!")
        return res



def _pipeline(path,importer,features,filters):

    data = importer._get_data(iterator = path)
    iswin = importer.iswin

    keys = list(data.keys())
    rec_name = keys[0]
    fs = data['fs']
    data_val = data[rec_name]

    if filters is not None:
        data_val = apply_filters(filter_obj=filters,data=data_val,fs=fs)
    
    if len(data)>3:
        res = _extract_features(feature_obj=features,data=data_val,fs=fs, win_len=data['win_len'], time_stamps=data['time_stamps'])
    else:
        res = _extract_features(feature_obj=features,data=data_val,fs=fs)
    
    
    if iswin:
        index = data['window']
        res = {'ID':rec_name, **res}
    else:
        index = rec_name

    return index,res


