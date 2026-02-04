'''
Docstring for module1.Coffee_Machine
You're task is to create a coffee machine by extending the base function(coffee machine) using decorators. A decorator is a way of extending a base function without modifying it.

To complete this exercise there are 4 sub tasks:

Create a basic function that prints out a string such as: "Here is your coffee".

Create a decorator by nesting a wrapper function within it.

Add the decorator to the base function.

Add arguments to your base function by utilising 'args & kwargs', then set up your wrapper function to accept arguments.
'''


def add_milk(func):
    def wrapper(*args,**kwargs):
        print("You add milk")
        func(*args,**kwargs)
    return wrapper

def add_sugar(func):
    def wrapper(*args,**kwargs):
        print("you add sugar")
        func(*args,**kwargs)
    return wrapper

@add_milk
@add_sugar
def get_coffee(type_of_coffee):
    print(f"Here is your {type_of_coffee}, enjoy!")

get_coffee("Expresso")    

get_coffee("Cappuccino")
            