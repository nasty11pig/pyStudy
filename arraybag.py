# -*- coding: utf-8 -*-
"""
Created on Sat May 12 20:01:26 2018

@author: zjy
"""

from arrays import Array

class ArrayBag(object):
    """AN array-based bag implementation"""
    
    DEFAULT_CAPACITY = 10
    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    
    def __len__(self):
        return self._size
    
    def add(self, item):
        self._items[len(self)] = item
        self._size += 1
        
    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1