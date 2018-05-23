# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:26:39 2018

@author: zjy
"""

from array import Array
from abstractbag import AbstractBag


class ArrayBag(AbstractBag):
    
    DEFAULT_CAPACITY = 10
    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayBag.DEFAULT_CATACITY)
        AbstractBag.__init(self, sourceCollection)
    

    
    def __iter__(self):
        cursor = 0 
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1 
    
    def add(self, item):
        self._items[len(self)] = item
        self._size += 1
    
    def remove(self, item):
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex, len(self)):
            self._items[i] = self._items[i+1]
        self._size -= 1
        return True 
    
    def __clear__(self):
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
            
    def __str__(self):
        return "{" + ",".join(map(str, self)) + "}"
    
