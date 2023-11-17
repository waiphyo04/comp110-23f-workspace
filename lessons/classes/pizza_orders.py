"""Instantiating a class"""
"""
This is where we instantiate the class we defined in classes.py.
In other words, we are creating objects that belong to that class
"""

#import the class
#from <file_name>.<module_name> import <class_name>
from lessons.classes.pizza import Pizza 

my_pizza: Pizza = Pizza("large", 10, True) #Constructor 

#accessing or setting attributes
#my_pizza.size = "medium"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True 

#printing out some values 
print("my_pizza: ")
print(my_pizza)

print("Pizza: ")
print(Pizza)

print("Size Attribute: ")
print(my_pizza.size)

print("Toppings: ")
print(my_pizza.toppings)

print("gluten free: ")
print(my_pizza.gluten_free)

sals_pizza: Pizza = Pizza("medium", 5, False)
#print(sals_pizza.size)
#print(sals_pizza.toppings)
#print(sals_pizza.gf)

def price(input_pizza: Pizza) -> float:
    """Function to calculate Price of Pizza"""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00 
    return price 
#Calling function
print(price(sals_pizza))
print(price(my_pizza))

#Calling price method 
print(sals_pizza.price())
print(my_pizza.price())

#my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)

print(my_other_pizza.toppings)
print(my_pizza.toppings)