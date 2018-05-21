# -*- coding: utf-8 -*-
"""
Created on Mon May 21 20:49:08 2018

@author: zjy
"""

from abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):
    
    def __init__(self, sourceCollection = None):
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    
    def add(self, item):
        pass