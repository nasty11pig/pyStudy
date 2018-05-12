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


class TwoWayNode(Node):
    
    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous
        

head = TwoWayNode(1)
tail = head

for data in range(2,6):
    tail.next = TwoWayNode(data,tail)
    tail = tail.next
    

probe = tail
while probe != None:
    print(probe.data)
    probe = probe.previous
    
