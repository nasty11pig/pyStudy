# -*- coding: utf-8 -*-

from linkedquene import LindedQuene

class Cashier():
    
    def __init__(self):
        self._totalCustomerWaitTime = 0
        self._customersServed = 0
        self._currentCustomer = None
        self._quene = LinkedQuene()
        
    def addCustomer(self, c):
        self._quene.add(c)
        
    def serveCustomers(self, currentTime):
        if self._currentCustomer is None:
            if self._quene.isEmpty():
                return
            else:
                self._currentCustomer = self._quene.pop()
                self._totalCustomerWaitTime += currentTime - \
                    self._currentCustomer.arrivalTime()
                self._customersServed += 1
        
        self._currentCustomer.serve()
        if self._currentCustomer.amountofServiceNeeded() == 0:
            self._currentCustomer = None
    
    def __str__(self):
        result = "TOTALS FOR THE CASHIER\N" + \
                "Number of customers served:" + \
                str(self._customersServed) = "\n"
        if self._customerServed != 0:
            aveWaitTime = self._totalCustomerWaitTime / self._customersServed
            result += "Number of customers left in quene: "\
                    + str(len(self._quene)) + "\n" \
                    + "Average time customers spend\n" + \
                    "waitine to be served: " + "%5.2f" % aveWaitTime
        return result
    
                    