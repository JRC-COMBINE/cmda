import os
from functools import partial
from tqdm import tqdm
import concurrent

import numpy as np
import pandas as pd
import datetime
from typing import Optional


class ReadCSV:
    def __init__(
        self, files_list, channels = None, fs: int = 1, **kwargs
    ):
        '''
        Read multiple signals with CSV formats.

        The module imports signals (time-series) database with csv format, 
        where each CSV files columns represent the signals and rows the time instances.

        Args:
            files_list ({str} or {list}): list of CSV files' paths or the path
                to directory containg the CSV files.
            channels (list, optional): list of the column names (signals) to import. 
                If None, all the columns are imported. Defaults to None.
            fs (int, optional): Sampling frequency of the data. Defaults to 1.
        '''    
        self.channels = channels
        self.kwargs = kwargs
        self.fs = fs
        self.iswin = False
        self.iterator = self._iterator(files_list=files_list)

    def load(self,n_jobs=None):
        '''
        load the data.

        Args:
            n_jobs (int, optional): The number of OpenMP processes to use for reading the data. 
            ```None``` means using all processors. Defaults to None.

        Returns:
            dict: imported data as a dictionary, where the keys are the record names.
        '''        
        iterator = self.iterator
        if n_jobs == 1:
            iterator_progress = tqdm(iterator)
            res = map(self._get_data, iterator_progress)
        else:
            executer = concurrent.futures.ProcessPoolExecutor(max_workers= n_jobs)
            res = tqdm(executer.map(self._get_data, iterator), total=len(iterator))

        return list(res)


    def _get_data(self, iterator):
        res = pd.read_csv(iterator, usecols=self.channels, **self.kwargs)
        res = res.to_dict("list")

        record_name = os.path.basename(iterator)[:-4]
        res = {record_name: res, "fs": self.fs, "window": None}
        return res

    def _iterator(self, files_list):
        if isinstance(files_list, list):
            res = files_list
        elif isinstance(files_list, str):
            if os.path.isdir(files_list):
                res = [
                    os.path.join(files_list, f)
                    for f in os.listdir(files_list)
                    if f.endswith("csv")
                ]
            else:
                raise TypeError(
                    "files_list must be either a list of 'csv' files of a directory path of 'csv' files"
                )
        return res


class RollingWindowCSV:
    def __init__(
        self,
        files_list = None,
        win_len = None,
        step=None,
        channels= None,
        fs= 1,
        time_index_col= None,
        datetime_format= None,
        iterator = None,
        **kwargs
    ):
        '''
        Read multiple CSV formats with segmentation.

        The module imports signals (time-series) database with csv format and 
        segments them in a rolling window manner.
        where each CSV files columns represent the signals and rows the time instances.

        Args:
            files_list ([type]): files_list ({str} or {list}): list of CSV files' paths or the path
                to directory containg the CSV files.
            win_len (float): length of window in seconds.
            step (float, optional): length of moving window steps in seconds. 
                If None, the step length is equalt to the window length. Defaults to None.
            channels (list, optional): list of the column names (signals) to import. 
                If None, all the columns are imported. Defaults to None.
            fs (int, optional): sampling frequency of the data. Defaults to 1.
            time_index_col (str,optional): name of date_time column in the rae CSV files
            datetime_format (str,optional): format of the date_time if time_index_col is given
            iterator (list,optional): list of iterators for importing the CSV files. if given, other inputs will be ignored
        '''    
        self.channels = channels
        self.kwargs = kwargs
        self.win_len = win_len
        if step:
            self.step = step
        else:
            self.step = win_len
        self.fs = fs
        self.iswin = True
        self.time_index_col = time_index_col
        self.datetime_format = datetime_format

        if iterator is None:
            self.iterator = self._iterator(files_list=files_list)
        else:
            self.iterator = iterator

    def _get_data(self, iterator):
        path = iterator[0]
        time_stamps = None
        if iterator[1].size > 0:
            bin_win = np.array(iterator[1])+1
            bin_win = set(bin_win)
            len_data = set(range(1, iterator[2]+1))
            skip_rows = len_data.difference(bin_win)
            if self.time_index_col:
                usecols = self.channels.copy()
                usecols.append(self.time_index_col)
                res = pd.read_csv(path, skiprows=skip_rows, usecols=usecols, **self.kwargs)
                time_idx = pd.to_datetime(res[self.time_index_col], format=self.datetime_format)
                # window_name = time_idx.iloc[0]
                time_idx = time_idx -time_idx.iloc[0]
                time_stamps = np.array([i.total_seconds() for i in time_idx])
                res.drop(columns=[self.time_index_col], inplace=True)
                
            else:
                res = pd.read_csv(path, skiprows=skip_rows, usecols=self.channels, **self.kwargs)
                # window_name = iterator[1][0]
        else:
            temp = np.repeat(np.nan,len(self.channels))
            res = pd.DataFrame(temp.reshape(-1,len(temp)),columns=self.channels)
        res = res.astype('float')
        res = res.to_dict("list")

        record_name = os.path.basename(path)[:-4]
        res = {
            record_name: res,
            "fs": self.fs,
            "win_len" : self.win_len,
            "time_stamps" : time_stamps,
            "window": iterator[4],
        }
        return res

    def load(self,n_jobs=None):
        '''
        load the data

        Args:
            n_jobs (int, optional): The number of OpenMP processes to use for reading the data. 
            ```None``` means using all processors. Defaults to None.

        Returns:
            dict: imported data as a dictionary, where the keys are the record names.
        '''        
        iterator = self.iterator
        if n_jobs == 1:
            iterator_progress = tqdm(iterator)
            res = map(self._get_data, iterator_progress)
        else:
            executer = concurrent.futures.ProcessPoolExecutor(max_workers= n_jobs)
            res = tqdm(executer.map(self._get_data, iterator), total=len(iterator))

        return list(res)

    def _iterator(self, files_list):
        if isinstance(files_list, list):
            itr = files_list
        elif isinstance(files_list, str):
            if os.path.isdir(files_list):
                itr = [
                    os.path.join(files_list, f)
                    for f in os.listdir(files_list)
                    if f.endswith("csv")
                ]
            else:
                raise TypeError(
                    "files_list must be either a list of 'csv' files of a directory path of 'csv' files"
                )

        iterator = []
        for file in itr:
            if self.time_index_col:
                time_idx = pd.read_csv(file,usecols=[self.time_index_col], **self.kwargs)
                time_idx = pd.to_datetime(time_idx['ChartTime'], format=self.datetime_format)
                n_lines = len(time_idx)
                t_l = time_idx.iloc[0]
                bins = []
                while t_l < time_idx.iloc[-1]:
                    t_h = t_l +datetime.timedelta(seconds=self.win_len)
                    win = np.array(time_idx[(time_idx>=t_l) & (time_idx<t_h)].index)
                    bins.append((t_l,t_h,win))
                    t_l = t_l +datetime.timedelta(seconds=self.step)
            else:
                n_lines = sum(1 for line in open(file)) - 1
                bins = get_bins(n=n_lines, win_len=self.win_len, step=self.step, fs=self.fs)
            
            for t_l,t_h,win in bins:
                iterator.append((file, win, n_lines,t_l,t_h))

        return iterator





def get_bins(n, win_len, step=None, fs=1):

    if step is None:
        step = win_len

    # TODO: add warning in case of bin_lin > n
    # TODO: action to the last bin
    win_len = int(win_len * fs)
    step = int(step * fs)
    n_bins = int(np.floor((n - win_len) / step) + 1)
    bins = [(i * step,(i * step) + win_len,range((i * step), (i * step) + win_len)) for i in range(0, n_bins)]
    return bins


class ReadFeather:
    def __init__(self, files_list, channels: Optional[list] = None, **kwargs):
        self.channels = channels
        self.iswin = False

        if isinstance(files_list, list):
            self.iterator = files_list
        elif isinstance(files_list, str):
            if os.path.isdir(files_list):
                self.iterator = [
                    f for f in os.listdir(files_list) if f.endswith(".feather")
                ]
            else:
                raise TypeError(
                    "files_list must be either a list of 'feather' files of a directory path of 'feather' files"
                )

    def _get_data(self, path):
        res = pd.read_feather(path)
        return res