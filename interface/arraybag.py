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
    
    def __len__(self):
        return self._size
    
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
        for i in range(tagetindex, len(self)):
            self._items[i] = self._items[i+1]
        self._size -= 1
    
    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True
    
    def __clear(self):
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
            
    def isEmpty(self):
        return self._size == 0
    
    def __str__(self):
        return "{" + ",".join(map(str, self)) + "}"
    
    def __add__(self, other):
        pass
    