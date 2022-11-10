#CustomPizza.py
from Pizza import *
class CustomPizza(Pizza):
    def __init__(self, size):
        super(CustomPizza, self).__init__(size)
        self.toppingson = ""
        if self.getSize() == "S":
            self.setPrice(8.00)
        if self.getSize() == "M":
            self.setPrice(10.00)
        if self.getSize() == "L":
            self.setPrice(12.00)

    def addTopping(self, topping):
        self.toppingson += "\t+ " + topping + "\n"
        if self.getSize() == "S":
            newprice = self.getPrice() + 0.5
            self.setPrice(newprice)
        elif self.getSize() == "M":
            newprice = self.getPrice() + 0.75
            self.setPrice(newprice)
        else:
            newprice = self.getPrice() + 1
            self.setPrice(newprice)

    def getPizzaDetails(self):
        return "CUSTOM PIZZA\nSize: {}\nToppings:\n{}Price: ${:0.2f}\n".format(self.size, self.toppingson, self.price)