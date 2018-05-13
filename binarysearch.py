# -*- coding: utf-8 -*-
"""
Created on Sun May 13 21:31:30 2018

@author: zjy
"""
def binarySearch(target, sortedLyst):
    
    left = 0 
    right = len(sortedLyst)
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1


if __name__ == '__main__':
    sortedLyst = list(range(3,9))
    print(sortedLyst, binarySearch(5,sortedLyst))
        
    
        