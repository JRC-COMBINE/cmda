

import numpy as np

from ._add_functions import AddFeatures

class Features:

    _udf_list = {}

    def __init__(self):
        self.add_feature = AddFeatures()
        self.features = {}


    @classmethod
    def add_fun(cls,name,fun,labels):
        name2 = "__"+name
        name3 = "_Features"+name2      
        setattr(cls,name3,decorator_fun(fun,labels))
        cls._udf_list = {**cls._udf_list,**{name2:{}}}


    def apply_features(self,x,fs):
        self.x = x
        self.fs = fs
        self._features = {**self.add_feature._ListOfFunctions,**self._udf_list}
        for key in self._features:
            temp_key = key
            temp_value = self._features[key]
            self2 = '_Features'+ temp_key
            method_to_call = getattr(self, self2)
            #method_to_call(self.x)
            if len(temp_value) == 0:
                method_to_call()
            else:
                method_to_call(**self.add_feature._ListOfFunctions[key])

    def __mean(self):
        out = np.mean(self.x)
        out = {'mean':out}
        self.features = {**self.features, **out}

    def __max(self):
        out = np.max(self.x)
        out = {'max':out}
        self.features = {**self.features, **out}

    def __statistic(self):
        out1 = np.median(self.x)
        out2 = np.std(self.x)
        out = {'median':out1,'std':out2}
        self.features = {**self.features, **out}


def decorator_fun(fun,labels):
    if not isinstance(labels,(list,tuple)):
        labels = [labels]
    def wrapper_fun(self):
        out = fun(x = self.x)
        if not isinstance(out,(list,tuple)):
            out = [out]
        out = dict(zip(labels,out))
        self.features = {**self.features,**out}
    return wrapper_fun






if __name__ == "__main__":
    x = [1,2,3,4,5,6]

    def fun1(x,y=4):
        return np.min(x), np.std(x)

    labels = ('min','std')

    a = Features(x)
    a.add_feature.mean()
    a.add_feature.max()
    a.add_fun('udf',fun1,labels)
    a.apply_features()

    print(a._features)
    print(a.features)

