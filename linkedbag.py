# -*- coding: utf-8 -*-
"""
Created on Sat May 12 21:40:08 2018

@author: zjy
"""

from node import Node

class LinkedBag():
    
    def __init__(self, sourceCollection = None):
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
                
    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1
    
    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next
    
    def __getitem__(self, index):
        pass