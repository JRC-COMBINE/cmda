import os

import numpy as np
import pandas as pd
from typing import Optional
import wfdb




class ReadWFDB:

    def __init__(self, channels: Optional[list] = None):
        self.channels = channels

    def _get_data(self,rec_path,pb_dir,sampfrom=0,sampto=None):
        res = _read_wfdb(
            record_path= rec_path,
            pb_dir = pb_dir,
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
        pb_dir (str): wfdb.rdrecord pb_dir input
    """
    if not isinstance(source, (str, None)):
        raise TypeError("Source must be either str or None")

    if source is None:
        record_path = rec_name
        pb_dir = rec_path
    else:
        record_path = os.path.join(source, rec_path, rec_name)
        pb_dir = None

    return rec_path, pb_dir


def _get_rec_info(record_path: str, pb_dir: str) -> tuple:
    """
    Get the record name, sampling frequency of the signals,
    signals length and available signal channels.

    Args:
        record_path (str): wfdb.rdrecord record_name input
        pb_dir (str): wfdb.rdrecord pb_dir input

    Returns:
        sig_len (int): Signals' ndarray length
        sig_name (list): Signals' names
        fs (float): Signals' sampling frequency
    """

    # get the header of wfdb record
    rec_info = wfdb.rdheader(record_name=record_path, pb_dir=pb_dir)

    record_name = rec_info.record_name
    sig_len = rec_info.sig_len
    sig_name = rec_info.sig_name
    fs = rec_info.fs

    return record_name, sig_len, sig_name, fs


def _read_wfdb(
    record_path: str,
    pb_dir: Optional[str] = None,
    channel_names: Optional[list] = None,
    sampfrom: int = 0,
    sampto: Optional[int] = None,
):

    # get the wfdb record information
    record_name, sig_len, sig_name, fs = _get_rec_info(
        record_path=record_path, pb_dir=pb_dir
    )

    # TODO check the channel names
    if channel_names is None:
        channel_names = sig_name


    record = wfdb.rdrecord(
        record_name=record_path,
        pb_dir=pb_dir,
        sampfrom=sampfrom,
        sampto=sampto,
        channel_names=channel_names,
    )

    data = record.p_signal
    data = dict(zip(channel_names, data.transpose()))

    res = {record_name: data, 'fs':fs}

    return res


if __name__ == "__main__":
    record_path = (
        "/Users/pejman/Desktop/CPMA_Project/ptb/data/ptb-xl/records500/05000/05460_hr"
    )
    pb_dir = None

    data = _read_wfdb(record_path=record_path, pb_dir=None)
    print(data.keys())
