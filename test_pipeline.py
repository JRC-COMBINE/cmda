import numpy as np
import pandas as pd
import os
import time
from functools import partial
import concurrent.futures
from multiprocessing import Pool

from cmda.data_import.import_wfdb import ReadWFDB
from cmda.data_import.import_local import ReadCSV
from cmda.feature_extraction import Features
from cmda.feature_extraction.feature_extraction import Pipeline, _pipeline
from cmda.feature_extraction.feature_extraction import FeatureExtraction

# data
metadata = pd.read_csv('/Users/pejman/Desktop/CPMA_Project/ptb/metadata/ptbxl_database.csv')
file_names = metadata['filename_hr'][0:10]
source = '/Users/pejman/Desktop/CPMA_Project/ptb/data/ptb-xl'

rec_paths = []
for name in file_names:
    rec_paths += [os.path.join(source,name)]


# features
def fun1(x,y=4):
    return np.min(x), np.std(x)

labels = ('min','std')

feature_obj = Features()
feature_obj.add.mean()
feature_obj.add.max()




# Importer
importer = ReadWFDB(rec_path_list=rec_paths,pb_dir=None)
# features = FeatureExtraction(feature_obj=feature_obj)


# start = time.perf_counter()
# a = Pipeline(importer=importer,features=feature_obj)
# res = a.run()
# end = time.perf_counter()
# print(end-start)
# print(len(res))

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
files = files[0:10]

importer = ReadCSV(files_list=files)


a = Pipeline(importer=importer,features=feature_obj)
res = a.run_p(n_jobs=2)

print(res)
# iterator = list(enumerate(iterator))
# print(iterator)
# pip_func = partial(_pipeline, importer = importer, features = feature_obj)

# with Pool(3) as p:
#     res = p.map(pip_func,importer.iterator)


# print(list(res))