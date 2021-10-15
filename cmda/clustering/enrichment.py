
import numpy as np
import pandas as pd

from scipy.stats import chi2_contingency, fisher_exact


def cluster_enrichment(true_labels,pred_labels, normalize = 'pred', binary = False, scaled = False):
    if not isinstance(true_labels,pd.DataFrame):
        raise TypeError('true labels must be Dataframe')

    con_table = {}
    con_table_n = {}
    true_count = []
    p_value = []
    for col_t in true_labels:
        true = true_labels[col_t]

        ct, ctn, tc, pc, p = _cluster_enrich_array(true,pred_labels,normalize=normalize, scaled = scaled)
        con_table[col_t] = ct
        con_table_n[col_t] = ctn
        true_count.append(tc)
        p_value.append(p)


    con_table = pd.concat(con_table.values(), axis=0, keys = con_table.keys())
    con_table_n = pd.concat(con_table_n.values(), axis=0, keys = con_table_n.keys())
    if binary:
        con_table.drop([0], level=1, inplace=True)
        con_table_n.drop([0], level=1, inplace=True)
    true_count = pd.DataFrame(true_count, index = true_labels.columns)
    pred_count = pd.DataFrame(pc, columns = ['number'])
    pred_count = pred_count.T
    p_value = pd.DataFrame(p_value, index = true_labels.columns)
    
    
    return con_table, con_table_n, true_count, pred_count, p_value


def _cluster_enrich_array(true_labels,pred_labels, normalize = 'pred', scaled = False):

    true_labels = np.array(true_labels, dtype='object')
    num_true_l = len(np.unique(true_labels))
    true_count = pd.value_counts(true_labels,sort=False)


    pred_labels = np.array(pred_labels, dtype='object')
    pred_count = pd.value_counts(pred_labels,sort=False)

    con_table = pd.crosstab(true_labels,pred_labels,rownames=['true'],colnames=['pred'])

    enrich_func = fisher
    if num_true_l > 2:
        enrich_func = chi2_con

    p = []
    for col in con_table.columns:
        pred_ratio = con_table[col]/np.sum(con_table[col])
        true_ratio = true_count/np.sum(true_count)
        sign = np.sign(pred_ratio[1]-true_ratio[1]).sum()
        if scaled:
            pred_count_col = np.round(pred_ratio*true_count[0])
        else:
            pred_count_col = con_table[col]

        obs = np.array(pd.concat([pred_count_col,true_count], axis=1, sort=True))
        ps = enrich_func(obs)
        if ps==0:
            ps = 300
        else:
            ps = -np.log10(ps)

        p = np.append(p,ps*sign)


    if normalize == 'pred':
        con_table_n = con_table.div(con_table.sum(axis=0), axis=1)
    elif normalize == 'true':
        con_table_n = con_table.div(con_table.sum(axis=1), axis=0)
    elif normalize == 'all':
        con_table_n = con_table.div(np.sum(con_table.sum(axis=0)), axis=1)




    return con_table, con_table_n, true_count, pred_count, p




def chi2_con(obs):
    _,p,_,_ = chi2_contingency(obs, correction = False)
    return p

def fisher(obs):
    _,p = fisher_exact(obs)
    return p