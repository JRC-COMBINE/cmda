
import numpy as np 


class AddFeatures():   
    def __init__(self):
        self._ListOfFunctions = {}

    def mean(self,**kwargs):
        if '__mean' not in self._ListOfFunctions:
            self._ListOfFunctions['__mean'] = kwargs

    def max(self, **kwargs):
        if '__max' not in self._ListOfFunctions:
            self._ListOfFunctions['__max'] = kwargs
