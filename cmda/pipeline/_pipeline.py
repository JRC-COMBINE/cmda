import numpy as np
import pandas as pd

from functools import partial
from tqdm import tqdm
from pathos.multiprocessing import ProcessingPool as Pool


from ..feature_extraction.feature_extraction import _extract_features
from ..preprocessing.filter_object import apply_filters





class Pipeline:

    def __init__(self,importer,features, filters = None):
        '''
        genearte a pipeline for reading, filtering and extracting features from multiple temporal data files
        
        Args:
            importer (importer-object): created importer instance
            features (feature-object): created feature instance containg added feature functions
            filters (filter-object, optional): created filter instance containg added feature functions. Defaults to None.
        '''
        self.importer = importer
        self.features = features
        self.filters = filters


    def run(self, n_jobs = 1, dataframe_output = False):
        '''
        run the pipeline

        Args:
                       n_jobs (int,optional): Number of jobs to run in parallel. -1 means using all processors. Defaults to 1.
                       dataframe_output (True or False, optional): if True return the output in a dataframe format. Else the output is a dictionary. Defaults to True.
        '''

        # generate the iterators
        iterators = self.importer.iterators

        pip_func = partial(_pipeline, importer = self.importer, features = self.features, filters = self.filters)

        print(f"Running the pipeline on {len(iterators)} instances...\n")
        if n_jobs == 1:
            iterator_progress = tqdm(iterators)
            res = map(pip_func, iterator_progress)
        else:
            p = Pool()
            res = tqdm(p.map(pip_func, iterators),total=len(iterators))

        # create a dict from the result output and remove None values
        res = {i[0]:i[1] for i in res if i is not None}

        if dataframe_output:
            res = pd.DataFrame(res).T

        print("finished!")
        return res



def _pipeline(path,importer,features,filters):

    data = importer._get_data(iterator = path)

    keys = list(data.keys())
    rec_name = keys[0]
    fs = data['fs']
    data_val = data[rec_name]

    if filters is not None:
        data_val = apply_filters(filter_obj=filters,data=data_val,fs=fs)
    
    # in case of rolling window the length of data is 5
    # otherwise it's 2
    if len(data)>2:
        res = _extract_features(feature_obj=features,data=data_val,fs=fs, win_len=data['win_len'], time_stamps=data['time_stamps'])
        index = data['window']
        res = {'ID':rec_name, **res}
    else:
        res = _extract_features(feature_obj=features,data=data_val,fs=fs)
        index = rec_name

    return index,res


