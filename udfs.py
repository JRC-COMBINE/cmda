import numpy as np

def count(x):
    res = np.nansum(x)
    res = {'count':res}
    return res

def check_event(x):
    res = np.isfinite(x).any()
    res = int(res)
    res = {'event':res}
    return res

def periodic_time(x):
    t = np.nanmedian(x)
    sin = np.sin(np.pi*t/12)
    cos = np.cos(np.pi*t/12)

    res = {
        'sin' : sin,
        'cos' : cos
    }
    return res
