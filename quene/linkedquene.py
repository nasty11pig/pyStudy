# -*- coding: utf-8 -*-

from abstractcollection import AbstractCollection
from node import Node

class LinkedQuene(AbstractCollection):
    
    def __init__(self, sourcecellection = None):
        AbstractCollection.__init__(self, sourcecellection)
    
    def add(self, newItem):
        newNode = Node(newItem, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1
    
    def pop(self):
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem