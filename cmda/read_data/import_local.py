import os
from functools import partial

import numpy as np
import pandas as pd
from typing import Optional


class ReadCSV:

    def __init__(self, files_list, channels: Optional[list] = None, fs: int = 1, **kwargs):
        self.channels = channels
        self.kwargs = kwargs
        self.fs = fs
        self.iterator = self._iterator(files_list=files_list)

        

    def _get_data(self,path):
        res = pd.read_csv(path,**self.kwargs)
        res = res.to_dict('list')

        record_name = os.path.basename(path)
        res = {record_name: res, 'fs':self.fs}
        return res

    def _iterator(self,files_list):
        if isinstance(files_list,list):
            res = files_list
        elif isinstance(files_list,str):
            if os.path.isdir(files_list):
                iterator = [os.path.join(files_list,f) for f in os.listdir(files_list) if f.endswith('csv')]
            else:
                raise TypeError("files_list must be either a list of 'csv' files of a directory path of 'csv' files")
        return res


class ReadFeather:

    def __init__(self, files_list, channels: Optional[list] = None, **kwargs):
        self.channels = channels

        if isinstance(files_list,list):
            self.iterator = files_list
        elif isinstance(files_list,str):
            if os.path.isdir(files_list):
                self.iterator = [f for f in os.listdir(files_list) if f.endswith('.feather')]
            else:
                raise TypeError("files_list must be either a list of 'feather' files of a directory path of 'feather' files")


    def _get_data(self,path):
        res = pd.read_feather(path)
        return res