# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:49:37 2018

@author: zjy
"""

from arraybag import ArrayBag

class ArraySortedBag(ArrayBag):
    
    def __init__(self, sourcecollection = None):
        ArrayBag.__init__(self, sourcecollection)
    
    def __contains__(self, item):
        """
        二叉树搜索实现in方法
        """        
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left +right) // 2
            if item == self._items[mid]:
                return True
            elif item < self._items[mid]:
                right = mid + 1
            else:
                left = mid - 1
                 
    def add(self, item):        
        if self._isEmpty() or item >= self._items[len(self)-1]:
            ArrayBag.add(self, item)
        else:
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i-1]
            self._items[targetIndex] = item
            self._size += 1
    