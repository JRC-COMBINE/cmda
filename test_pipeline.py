import numpy as np
import pandas as pd
import os
import time
from functools import partial
import concurrent.futures
from multiprocessing import Pool

from cmda.read_data import RollingWindowWFDB, RollingWindowCSV, ReadCSV, ReadWFDB
# from cmda.read_data.import_local import ReadCSV
from cmda.feature_extraction import Features
from cmda.pipeline import Pipeline
from cmda.filter import Filters
# from cmda.feature_extraction.feature_extraction import Pipeline, _pipeline
# from cmda.feature_extraction.feature_extraction import FeatureExtraction

# data
metadata = pd.read_csv('/Users/pejman/Desktop/JRC/applications/ptb-xl/data/metadata/ptbxl_database.csv')
file_names = metadata['filename_hr']
source = "/Users/pejman/Desktop/JRC/applications/ptb-xl/data/ptb-xl"

rec_paths = []
for name in file_names:
    rec_paths += [os.path.join(source,name)]


# features
# def fun1(x,y=4):
#     return np.min(x), np.std(x)

# labels = ('min','std')

feature_obj = Features()
feature_obj.add.mnf()
feature_obj.add.mdf()
feature_obj.add.psr()
feature_obj.add.stdf()
feature_obj.add.peaks(n_peaks=3,spectrum='welch',height=False,width=False,nperseg=512)
feature_obj.add.band_power(low=0.6, high=2,spectrum='welch')
feature_obj.add.band_power(low=2, high=4,spectrum='welch')
feature_obj.add.band_power(low=4, high=6,spectrum='welch')
feature_obj.add.band_power(low=6, high=10,spectrum='welch')
feature_obj.add.band_power(low=10, high=15,spectrum='welch')
feature_obj.add.band_power(low=15, high=30,spectrum='welch')

filter_obj = Filters()
filter_obj.add.butter_filter(cutoff=0.5,order=5,btype='highpass')
filter_obj.add.butter_filter(cutoff=50,order=5,btype='lowpass')







importer = ReadWFDB(record_names=rec_paths,public_dir=None,channels=['II','I'])



start = time.perf_counter()
a = Pipeline(importer=importer,features=feature_obj, filters=filter_obj)
res = a.run(n_jobs=4,dataframe_output=True)
end = time.perf_counter()
print(end-start)
print(res)

# start = time.perf_counter()
# a = Pipeline(importer=importer,features=feature_obj)
# res = a.run_p()
# end = time.perf_counter()
# print(end-start)
# # print(list(res))
# print(res['00001_hr'])
# print(pd.DataFrame(res).T)

# source = "/Users/pejman/Desktop/CPMA_Project/hbedb/raw"
# files = [os.path.join(source,f) for f in os.listdir(source) if f.endswith('csv')]
# files = files[0:4]

# # importer = RollingWindowCSV(files_list=files,win_len=5, step=1,fs=1000)

# importer = ReadCSV(files_list=files)

# # a = Pipeline(importer=importer,features=feature_obj)
# # res = a.run(dataframe_output=True, n_jobs=4)

# res = importer.load(n_jobs=4)
# print(res[1])
# res = a.run_p(n_jobs=2)

# iterator = list(enumerate(iterator))
# print(iterator)
# pip_func = partial(_pipeline, importer = importer, features = feature_obj)

# with Pool(3) as p:
#     res = p.map(pip_func,importer.iterator)
 

