import os
import concurrent
from tqdm import tqdm
import numpy as np
import pandas as pd
from typing import Optional
import wfdb




class ReadWFDB:

    def __init__(self, record_names, pn_dir=None, channels=None):
        '''
        Read multiple records of a WFDB [(Physionet waveform database)].

        The module imports multiple records of a WFDB [(Physionet waveform database)] (https://physionet.org/about/database/)
        from either a local disk or Physionet server.

        Args:
            record_names (list): list of record names or records paths.
            public_dir ({str} or {list}, optional): in case of importing the data from Physionet server,
                public directory of the WFDB or list of public directories.
                For importing from a local disk, must be set to None. Defaults to None.
            channels (list, optional): list of the channel names (signals) to import. 
                If None, all the channels are imported. Defaults to None.
        '''   
        self.channels = channels
        self.iswin = False
        self.iterator = self._iterator(rec_path_list=record_names, pn_dir=pn_dir) 

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
        print("Loading the data ...")
        if n_jobs == 1:
            iterator_progress = tqdm(iterator)
            res = map(self._get_data, iterator_progress)
        else:
            executer = concurrent.futures.ProcessPoolExecutor(max_workers= n_jobs)
            res = tqdm(executer.map(self._get_data, iterator), total=len(iterator))

        return list(res)
    
    def _iterator(self,rec_path_list,pn_dir):
        # if rec_path_list is None:
        #     if pb_dir is None:
        #         raise ValueError("When recored_names is None, a public_dir must be set")
        #     else:
        #         rec_path_list = wfdb.io.get_record_list(db_dir=pb_dir)
        if not isinstance(pn_dir,list):
            iterator = tuple(map(lambda x: (x, pn_dir), rec_path_list))
        else:
            iterator = list(zip(rec_path_list,pn_dir))

        return iterator

    def _get_data(self,iterator,sampfrom=0,sampto=None):
        rec_path = iterator[0]
        pn_dir = iterator[1]
        res = _read_wfdb(
            record_path= rec_path,
            pn_dir = pn_dir,
            channel_names= self.channels,
            sampfrom = sampfrom,
            sampto=sampto
        )

        return res



class RollingWindowWFDB:

    def __init__(self, record_names, public_dir, win_len, step=None, channels=None):
        '''
        Read multiple records of a WFDB [(Physionet waveform database)].

        The module imports multiple records of a WFDB [(Physionet waveform database)] (https://physionet.org/about/database/)
        from either a local disk or Physionet server.

        Args:
            record_names (list): list of record names or records paths.
            public_dir ({str} or {list}, optional): in case of importing the data from Physionet server,
                public directory of the WFDB or list of public directories.
                For importing from a local disk, must be set to None. Defaults to None.
            win_len (float): length of window in seconds.
            step (float, optional): length of moving window steps in seconds. 
                If None, the step length is equalt to the window length. Defaults to None.
            channels (list, optional): list of the channel names (signals) to import. 
                If None, all the channels are imported. Defaults to None.
        '''  
        self.channels = channels
        self.win_len = win_len
        self.step = step
        self.iswin = True
        self.iterator = self._iterator(rec_path_list=record_names, pn_dir=public_dir) 

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
    
    def _iterator(self,rec_path_list,pn_dir):
        if not isinstance(pn_dir,list):
            itr = list(map(lambda x: (x, pn_dir), rec_path_list))
        else:
            itr = list(zip(rec_path_list,pn_dir))

        iterator = []
        print("Initializing the segmentation ...")
        for rec_path,pb in itr:
            record_name, sig_len, sig_name, fs = _get_rec_info(
                record_path=rec_path, pn_dir=pb
            )

            bins = get_bins(n = sig_len, win_len = self.win_len, step = self.step, fs = fs)

            for win in bins:
                iterator.append((rec_path,pb,win))

        return iterator


    def _get_data(self,iterator):
        rec_path,pn_dir,samples = iterator
        sampfrom = samples[0]
        sampto = samples[-1]

        res = _read_wfdb(
            record_path= rec_path,
            pn_dir = pn_dir,
            channel_names= self.channels,
            sampfrom = sampfrom,
            sampto=sampto
        )
        return res



    



def _get_rec_path(rec_name: str, rec_path: str, source: Optional[str] = None) -> tuple:
    """
    Get the record name, public directory, sampling frequency of the signals,
    signals length and available signal channels.

    Args:
        rec_name (str): record name
        rec_path (str): record path
        source (Optional[str], optional): local directory of wfdb files.
            If None, uses the record path as the public directory. Defaults to None.

    Raises:
        TypeError: Source must be either str or None

    Returns:
        record_path (str): wfdb.rdrecord record_name input
        pn_dir (str): wfdb.rdrecord pn_dir input
    """
    if not isinstance(source, (str, None)):
        raise TypeError("Source must be either str or None")

    if source is None:
        record_path = rec_name
        pn_dir = rec_path
    else:
        record_path = os.path.join(source, rec_path, rec_name)
        pn_dir = None

    return rec_path, pn_dir


def _get_rec_info(record_path: str, pn_dir: str) -> tuple:
    """
    Get the record name, sampling frequency of the signals,
    signals length and available signal channels.

    Args:
        record_path (str): wfdb.rdrecord record_name input
        pn_dir (str): wfdb.rdrecord pn_dir input

    Returns:
        sig_len (int): Signals' ndarray length
        sig_name (list): Signals' names
        fs (float): Signals' sampling frequency
    """

    # get the header of wfdb record
    rec_info = wfdb.rdheader(record_name=record_path, pn_dir=pn_dir)

    record_name = rec_info.record_name
    sig_len = rec_info.sig_len
    sig_name = rec_info.sig_name
    fs = rec_info.fs

    return record_name, sig_len, sig_name, fs


def _read_wfdb(
    record_path: str,
    pn_dir: Optional[str] = None,
    channel_names: Optional[list] = None,
    sampfrom: int = 0,
    sampto: Optional[int] = None,
):

    # get the wfdb record information
    record_name, sig_len, sig_name, fs = _get_rec_info(
        record_path=record_path, pn_dir=pn_dir
    )

    # TODO check the channel names
    if channel_names is None:
        channel_names = sig_name


    record = wfdb.rdrecord(
        record_name=record_path,
        pn_dir=pn_dir,
        sampfrom=sampfrom,
        sampto=sampto,
        channel_names=channel_names,
    )

    data = record.p_signal
    data = dict(zip(channel_names, data.transpose()))

    res = {record_name: data, 'fs':fs, 'window':(sampfrom,sampto)}

    return res


def get_bins(n, win_len, step = None, fs = 1):
    
    if step is None:
        step = win_len

    # TODO: add warning in case of bin_lin > n
    # TODO: action to the last bin
    win_len = int(win_len*fs)
    step = int(step*fs)
    n_bins = int(np.floor((n-win_len)/step)+1)
    bins = [range((i*step),(i*step)+win_len) for i in range(0,n_bins)]
    return bins



if __name__ == "__main__":
    record_path = (
        "/Users/pejman/Desktop/CPMA_Project/ptb/data/ptb-xl/records500/05000/05460_hr"
    )
    pn_dir = None

    data = _read_wfdb(record_path=record_path, pn_dir=None)
    print(data.keys())
