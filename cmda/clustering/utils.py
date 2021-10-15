import numpy as np 
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def label_corrector(x):
    original = list(set(x))
    mapped = list(range(len(x)))

    mapper = dict(zip(original,mapped))
    mapper[-1] = -1

    x = np.vectorize(mapper.get)(x)

    return x


def pca(X,n_components):
    x = X.copy()
    x = StandardScaler().fit_transform(x)
    res = PCA(n_components=n_components).fit_transform(x)
    return res