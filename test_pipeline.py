import numpy as np
import pandas as pd
import os
import time

from cmda.data_import.import_wfdb import ReadWFDB
from cmda.feature_engineering.feature_extraction import FeatureExtraction
from cmda.feature_engineering.feature_object import Features
from cmda.feature_engineering.feature_extraction import Pipeline


# data
metadata = pd.read_csv('/Users/pejman/Desktop/CPMA_Project/ptb/metadata/ptbxl_database.csv')
file_names = metadata['filename_hr']
source = '/Users/pejman/Desktop/CPMA_Project/ptb/data/ptb-xl'

rec_paths = []
for name in file_names:
    rec_paths += [os.path.join(source,name)]


# features
def fun1(x,y=4):
    return np.min(x), np.std(x)

labels = ('min','std')

feature_obj = Features()
feature_obj.add_feature.mean()
feature_obj.add_feature.max()
feature_obj.add_fun('udf',fun1,labels)



#Importer
importer = ReadWFDB()
features = FeatureExtraction(feature_obj=feature_obj)


# start = time.perf_counter()
# a = Pipeline(importer=importer,features=features)
# res = a.run(rec_path_list=rec_paths, pb_dir=None)
# end = time.perf_counter()
# print(end-start)
# print(len(res))

start = time.perf_counter()
a = Pipeline(importer=importer,features=features)
res = a.run_p(rec_path_list=rec_paths, pb_dir=None)
end = time.perf_counter()
print(end-start)
print(len(res))
print(res[1])

