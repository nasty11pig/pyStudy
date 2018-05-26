# -*- coding: utf-8 -*-

import random

class Customer():
    
    @classmethod
    def generateCustomer(cls, probabilityofNewArrival, 
                         arrivalTime, averageTimePerCustomer):
        if random.random() <= probabilityofNewArrival:
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None
        
    def __init__(self, arrivalTime, serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountofServiceNeeded = serviceNeeded
        
    def arrivalTime(self):
        return self._arrivalTime
    
    def amountofServiceNeeded(self):
        return self._amountofServiceNeeded
    
    def serve(self):
        self._amountofServiceNeeded -= 1