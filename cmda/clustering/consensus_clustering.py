import numpy as np 
import random
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from tqdm import tqdm

# from .utils import label_corrector, pca


from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, fcluster

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import time

def label_corrector(x):
    original = list(set(x))
    mapped = list(range(len(x)))

    mapper = dict(zip(original,mapped))
    mapper[-1] = -1

    x = np.vectorize(mapper.get)(x)

    return x


class ConsenusClustering:

    def __init__(self,n_clusters,algorithm = 'KMeans',threshold=0.3, n_it = 100, resampling_ratio=0.7):
        self.n_clusters = n_clusters
        if algorithm == 'KMeans':
            self.models = [KMeans(n_clusters=n_clusters)]
        elif algorithm == 'GaussianMixture':
            self.models = [GaussianMixture(n_components=n_clusters)]
               
        self.threshold = threshold
        self.resampling_ratio = resampling_ratio
        self.n_it = n_it

    def fit_predict(self,X):
        M = conensus_matrix(X,models=self.models, resampling_ratio=self.resampling_ratio, n_it=self.n_it)
        labels = hierarchical_clustering(M,n_clusters=self.n_clusters,threshold=self.threshold)
        self.score = score(M,labels)
        l = pd.DataFrame(labels)
        cl = l[0].value_counts()
        # cl = cl.to_dict()
        self.cl = cl

        return labels


def conensus_matrix(X,models,resampling_ratio=0.7,n_it=100):
    n = X.shape[0]
    dist = np.zeros(shape=(n,n))
    count = np.zeros(shape=(n,n))
    for _ in range(100):
        idx = random.sample(range(n),int(np.round(0.7*n)))

        X_idx = X[idx,:]
        model = random.choice(models)
        labels = model.fit_predict(X_idx)
        dist_sample = pdist(labels.reshape(-1,1))
        dist_sample[dist_sample!=0]=1
        dist_sample = squareform(dist_sample)

        dist[np.ix_(idx,idx)] = dist[np.ix_(idx,idx)] + dist_sample
        count[np.ix_(idx,idx)] += 1

    M = dist/count
    return M


def conensus_matrix_p(X,model,sampling_ratio=0.7,n_it=100, n_jobs=4):
    n = X.shape[0]
    pip_func = partial(con_mat,X=X,n=n, model=model, sampling_ratio=sampling_ratio)
    iterator = range(n_it)
    s = time.perf_counter()
    with ProcessPoolExecutor(max_workers = n_jobs) as executer:
        res = executer.map(pip_func, iterator)
    

    dist = np.zeros(shape=(n,n))
    count = np.zeros(shape=(n,n))
    print(time.perf_counter()-s)


    for idx,labels in res:
        dist_sample = pdist(labels.reshape(-1,1), metric='cityblock')
        dist_sample[dist_sample!=0]=1
        dist_sample = squareform(dist_sample)
        dist[np.ix_(idx,idx)] += dist_sample
        count[np.ix_(idx,idx)] += 1
    M = dist/count
    return res


def con_mat(iterator,X,n,model,sampling_ratio=0.7):
    idx = random.sample(range(n),int(np.round(sampling_ratio*n)))
    labels = model.fit_predict(X[idx,:])
    return idx,labels



def hierarchical_clustering(dist,n_clusters,method='ward', threshold=0.3):

    dist_flat = squareform(dist)

    hierarchy = linkage(dist_flat, method=method)
    labels = fcluster(hierarchy,t=n_clusters, criterion='maxclust')

    idx_out = find_unstable(M=dist,labels=labels, threshold=threshold)

    labels[idx_out] = -1
    labels = label_corrector(labels)

    return labels


def find_unstable(M,labels,threshold=0.3):
    idx_out = []
    for k in set(labels):
        idx = np.where(labels==k)[0]
        for i in idx:
            M_i = []
            for j in idx:
                if i!=j:
                    M_i.append(M[i,j])
            # M_k_i[i] = M_i
            if np.mean(M_i)>threshold:
                idx_out.append(i)

    return idx_out


def score(M,labels):
    score_k ={}
    for k in set(labels):
        idx = np.where(labels==k)[0]
        N = len(idx)
        M_k = 0
        for i in idx:
            M_i = []
            for j in idx:
                if i<j:
                    M_k += M[i,j]
        if N==1:
            score_k[k] = 1
        else:
            score_k[k] = 1-2*M_k/(N*(N-1))

    if -1 not in score_k.keys():
        score_k[-1] = 1

    return score_k










    




if __name__ == "__main__":
    X,y = make_blobs(n_samples=1000, n_features=10, centers=4, cluster_std=(4,12,14,4), random_state=42)
    # random_state = 49
    # n_samples = 5000
    # X = []
    # for i in range(20):
    #     n_features = np.random.choice((2,3,4,5,7),1)[0]
    #     n_centers = np.random.choice((1,1,1,2,3,4,5),1)[0]
    #     cluster_std = np.random.choice(np.linspace(1,6,51),n_centers)
    #     # print(n_features,n_centers, cluster_std)
    #     X_i,y_i = make_blobs(n_samples=n_samples, n_features=n_features, 
    #                     centers=n_centers, cluster_std=cluster_std, random_state=random_state)
    #     y_i = y_i.reshape(-1,1)
    #     if i==0:
    #         X = X_i
    #         y = y_i
    #     else:
    #         X = np.concatenate([X,X_i],axis=1)
    #         y = np.concatenate([y,y_i],axis=1)

    # print(X.shape)


    models = [KMeans(n_clusters=4)]

    s = time.perf_counter()
    M = conensus_matrix(X=X,models=models, n_it=100)
    print(time.perf_counter()-s)

    # print('unparallel')
    # s = time.perf_counter()
    # M = conensus_matrix(X=X,model=model, n_it=100)
    # print(time.perf_counter()-s)


    # labels = hierarchical_clustering(M,n_clusters=4, thershold=0.15)

    # plt.scatter(X[:,0],X[:,1],c=labels)
    # plt.show()
    # print(labels)

    # C = MultiLevelConsensusClustering()
    # res = C.levels(X,n_components=30)

    # res = pd.DataFrame(res)
    # print('finished')

    # C = MultiLevelConsensusClustering()
    # X_p = pca(X,n_components=15)
    # print(X_p.shape)
    # labels,s,cl = C.cluster(X_p)
    # print(s)
    # print(cl)
