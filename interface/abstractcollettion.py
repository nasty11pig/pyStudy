# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:50:08 2018

@author: zjy
"""

class AbstractCollecttion(object):
    
    def __init__(self, sourceCollection = None):
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    
    def __str__(self):
        return "{" + ",".join(map(str, self)) + "}"
    
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(self, item)
        return result

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0