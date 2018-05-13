# -*- coding: utf-8 -*-
"""
Created on Sat May 12 19:39:04 2018

@author: zjy
"""

class Array(object):
    
    def __init__(self, capacity, fillValue = None):
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)
            
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __str__(self):
        return str(self._items)
    
    def __setitem__(self, index, newitem):
        self._items[index] = newitem