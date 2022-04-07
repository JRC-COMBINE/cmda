import pandas as pd






def _extract_features(feature_obj, data: dict, fs: int = 1, **kwargs) -> dict:
    """
    Extarct features from a dictionary containing multiple arrays.

    Args:
        feature_obj (python_object): Feature object
        data (dict): Dictionary containing multiple arrays
        fs (int, optional): Sampling frequency of the arrays. Defaults to 1.

    Returns:
        dict: Extracted features
    """
    if isinstance(feature_obj,dict):
        features_keys = set(feature_obj.keys())
        data_keys = set(data.keys())
        if len(data_keys.difference(features_keys)) != 0:
            raise ValueError('The feature object keys are not as same as the data keys')

    res = {}
    for key, x in data.items():

        if isinstance(feature_obj,dict):
            obj = feature_obj[key]
        else:
            obj = feature_obj

        
        res_key = obj.transform(x = x, fs = fs, **kwargs)
        res_key = {f'{key}_{k}': v for k, v in res_key.items()}
        res = {**res,**res_key}

    return res


def extract_features(feature_obj, data: (dict,pd.DataFrame), fs: int = 1) -> dict:
    '''
    Extarct features from columns of a dataframe.

    Args:
        feature_obj (python_object): Feature object
        df (pd.DataFrame): Dataframe, where each column represents an array
        fs (int, optional): Sampling frequency of the arrays. Defaults to 1.

    Returns:
        dict: [description]
    '''

    if isinstance(data,pd.DataFrame):
        data = data.to_dict('list')

    res = _extract_features(
        feature_obj=feature_obj,
        data=data,
        fs=fs
    )

    return res
