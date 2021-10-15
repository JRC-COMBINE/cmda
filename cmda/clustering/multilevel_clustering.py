import numpy as np
import pandas as pd

from .consensus_clustering import ConsenusClustering
from .utils import pca, label_corrector


class MultiLevelConsensusClustering:
    def __init__(
        self, n_clusters=[2, 3], algorithm='KMeans', n_levels=2, threshold=0.3, n_it=100
    ):
        self.n_clusters = n_clusters
        self.algorithm = algorithm
        self.n_levels = n_levels
        self.threshold = threshold
        self.n_it = n_it

    def fit_predict(self, X, n_components, max_out=100):
        level_labels = {}
        level_labels[0] = np.repeat(0, X.shape[0])

        for l in range(self.n_levels):
            print("level: ", l)

            labels_l = level_labels[l].copy()
            labels_l_n = level_labels[l].copy()

            cl = pd.DataFrame(labels_l)
            cl = cl[0].value_counts()
            print(cl)

            l_offset = 0
            for k in set(labels_l):
                if k != -1:
                    idx = np.where(labels_l == k)[0]
                    print(k, "len_idx: ", len(idx))
                    X_p = pca(X[idx], n_components=n_components)

                    labels, score_m, cl = _k_cluster(
                        X=X_p,
                        algorithm=self.algorithm,
                        n_clusters=self.n_clusters,
                        threshold=self.threshold,
                        n_it=self.n_it,
                    )
                    print(l, k, score_m, cl)

                    best_k = min(cl, key=cl.get)

                    if cl[best_k] < max_out:
                        labels = labels[best_k]
                        labels[labels != -1] += l_offset
                        labels_l_n[idx] = labels

                    labels_l_n = label_corrector(labels_l_n)

                    l_offset = max(labels_l_n) + 1
                    print(l, k, set(labels), set(labels_l_n), l_offset)

            level_labels[l + 1] = labels_l_n

        return level_labels


def _k_cluster(X, n_clusters=[2, 3, 4], algorithm = 'KMeans', threshold=0.3, n_it=100):

    labels = {}
    cl = {}
    score_m = {}
    for n in n_clusters:
        C = ConsenusClustering(
            n_clusters=n, algorithm=algorithm, threshold=threshold, n_it=n_it
        )

        # self.labels[n] = C.fit_predict(X)
        # self.score[n] = C.score
        # self.cl[n] = C.cl
        labels[n] = C.fit_predict(X)
        try:
            score_m[n] = C.score[-1]
            # score_m[n] = np.mean(list(C.score.values()))
            cl[n] = C.cl[-1]
        except:
            score_m[n] = 1
            cl[n] = 0
    return labels, score_m, cl


