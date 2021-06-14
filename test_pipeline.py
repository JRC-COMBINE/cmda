import numpy as np
import pandas as pd
import os
import time
from functools import partial
import concurrent.futures
from multiprocessing import Pool

from cmda.read_data import RollingWindowWFDB, RollingWindowCSV, ReadCSV
# from cmda.read_data.import_local import ReadCSV
from cmda.feature_extraction import Features
from cmda.pipeline import Pipeline
# from cmda.feature_extraction.feature_extraction import Pipeline, _pipeline
# from cmda.feature_extraction.feature_extraction import FeatureExtraction

# data
# metadata = pd.read_csv('/Users/pejman/Desktop/CPMA_Project/ptb/metadata/ptbxl_database.csv')
# file_names = metadata['filename_hr'][0:4]
# source = '/Users/pejman/Desktop/CPMA_Project/ptb/data/ptb-xl'

# rec_paths = []
# for name in file_names:
#     rec_paths += [os.path.join(source,name)]


# features
# def fun1(x,y=4):
#     return np.min(x), np.std(x)

# labels = ('min','std')

feature_obj = Features()
feature_obj.add.mean()
feature_obj.add.max()




# Importer
# importer = RollingWindowWFDB(record_names=rec_paths,public_dir=None,channels=['II','I'], win_len=5,step=None)



# start = time.perf_counter()
# a = Pipeline(importer=importer,features=feature_obj)
# res = a.run()
# end = time.perf_counter()
# print(end-start)
# print(res)

# start = time.perf_counter()
# a = Pipeline(importer=importer,features=feature_obj)
# res = a.run_p()
# end = time.perf_counter()
# print(end-start)
# # print(list(res))
# print(res['00001_hr'])
# print(pd.DataFrame(res).T)

source = "/Users/pejman/Desktop/CPMA_Project/hbedb/raw"
files = [os.path.join(source,f) for f in os.listdir(source) if f.endswith('csv')]
files = files[0:4]

# importer = RollingWindowCSV(files_list=files,win_len=5, step=1,fs=1000)

importer = ReadCSV(files_list=files)

# a = Pipeline(importer=importer,features=feature_obj)
# res = a.run(dataframe_output=True, n_jobs=4)

res = importer.load(n_jobs=4)
print(res[1])
# res = a.run_p(n_jobs=2)

# iterator = list(enumerate(iterator))
# print(iterator)
# pip_func = partial(_pipeline, importer = importer, features = feature_obj)

# with Pool(3) as p:
#     res = p.map(pip_func,importer.iterator)
 

