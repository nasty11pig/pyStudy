# -*- coding: utf-8 -*-



class MarketModel():
    
    def __init__(self, lengthofSimulation, averageTimePerCus, 
                 probabilityofNewArrival):
        self._probabilityofNewArrival = probabilityofNewArrival
        self._averageTimeperCus = averageTimePerCus
        self._lenthofSimulation = lengthofSimulation
        self._cashier = Cashier()
    
    def runSimulation(self):
        for currentTime in range(self._lengthofSimulation):
            customer = Customer.generateCustomer(
                    self._probabilityofNewArrival,
                    currentTime, 
                    self._arraveTimePerCus)
            if customer != None:
                self._cashier.addCustomer(customer)
            self._cashier.serveCustomers(currentTime)
        
    def __str__(self):
        return str(self._cashier)
            