# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def lenNode(self):
        prob = self
        if prob == None :
            return 0
        else:
            n = 1
            while prob.next != None:
                n += 1
                prob = prob.next
            return n
    
head = None    
for count in range(1, 6):
    head = Node(count, head)       


