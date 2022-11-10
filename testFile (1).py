#testFile.py
from Pizza import *
from CustomPizza import *
from PizzaOrder import *
from SpecialtyPizza import *
from OrderQueue import *

#Test CustomPizza Class
def test_CustomPizza():
    cp1 = CustomPizza("L")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n"
    
    cp1.addTopping("Mushrooms")
    cp1.addTopping("Pepperoni")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ Mushrooms\n\
\t+ Pepperoni\n\
Price: $14.00\n"
    
    cp1.addTopping("Bacon")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ Mushrooms\n\
\t+ Pepperoni\n\
\t+ Bacon\n\
Price: $15.00\n"

#Test SpecialtyPizza Class
def test_SpecialtyPizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"

    sp2 = SpecialtyPizza("M", "Pepperoni")
    assert sp2.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: Pepperoni\n\
Price: $14.00\n"

    sp3 = SpecialtyPizza("L", "Hawaiian")
    assert sp3.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: L\n\
Name: Hawaiian\n\
Price: $16.00\n"


#Test PizzaOrder Class
def test_PizzaOrder():

    cp1 = CustomPizza("S")
    cp1.addTopping("Extra Cheese")
    cp1.addTopping("Basil")
    sp1 = SpecialtyPizza("S", "Carne-less")
    order = PizzaOrder(240000)
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 240000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ Extra Cheese\n\
\t+ Basil\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-less\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

    cp2 = CustomPizza("L")
    cp2.addTopping("Artichoke")
    cp2.addTopping("Olives")
    sp2 = SpecialtyPizza("M", "David's Pizza")
    order.addPizza(cp2)
    order.addPizza(sp2)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 240000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ Extra Cheese\n\
\t+ Basil\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-less\n\
Price: $12.00\n\
\n\
----\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+Artichoke\n\
\t+Olives\n\
Price: $14.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: M\n\
Name: David's Pizza\n\
Price: $14.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $49.00\n\
******\n"   

#Test OrderQueue Class
def test_OrderQueue():
    bh = OrderQueue()
    cp1 = CustomPizza("L")
    cp1.addTopping("Artichoke")
    cp1.addTopping("Olives")
    sp1 = SpecialtyPizza("M", "David's Pizza")
    sp2 = SpecialtyPizza("L", "Mary's Pizza")
    bh.insert(cp1)
    bh.insert(sp1)
    bh.insert(sp2)
    assert bh.delMin() == cp1
    assert bh.delMin() == sp1
    assert bh.delMin() == sp2