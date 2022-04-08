import numpy as np

def rm_outlier(x,low,high):
    res = np.array([i if high >= i >= low else np.nan for i in x])
    return res

def rm_outlier_quantile(x,q_low,q_high):
    low = np.quantile(x,q_low)
    high = np.quantile(x,q_high)
    res = rm_outlier(x,low=low,high=high)
    return res
