#PizzaOrder.py
from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *

class PizzaOrder():
    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        finalprice = 0
        eachpizza = ""
        begLine = "******" + "\n" + "Order Time: " + str(self.time) + "\n"
        endLine = "\n" + "----" + "\n"
        for pizza in self.pizzas:
            eachpizza += pizza.getPizzaDetails() + endLine
            finalprice += pizza.getPrice()
        return begLine + eachpizza + "TOTAL ORDER PRICE: ${:0.2f}\n".format(finalprice) + "******" + "\n"