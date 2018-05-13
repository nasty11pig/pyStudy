# -*- coding: utf-8 -*-
"""
Created on Sun May 13 21:31:30 2018

@author: zjy
"""
from arrays import ArrayBag

class ArraySortedBag(ArrayBag):
    
    def __init__(self, sourceCollection):
        ArrayBag.__init__(self, sourceCollection)
        
    def add(self, item):
        targetIndex = 0 
        while item > self._items[targetIndex]:
            targetIndex += 1
        for i in range(len(self._items), targetIndex, -1):
            self._items[i] = self._items[i-1]
        self._items[targetIndex] = item
        self._size += 1
    
    def __contain__(self, item):
        left = 0 
        right = len(sortedLyst)
        while left <= right:
            midpoint = (left + right) // 2
            if target == sortedLyst[midpoint]:
                return True
            elif target < sortedLyst[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False
    