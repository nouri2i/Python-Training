'''
Docstring for module1.FavouriteThingsPart1
To tell us a little about yourself, why not give us a list of your favourite things.

Using what you've learned about *args, write a function that looks like this:

  favourite_things(item1, item2, etc...) 
That returns your favourite things and how many you have listed as shown in the format below
EXAMPLE:
        favourite_things("chocolate", "videogames", "holidays", "relaxing")
OUTPUT:
       One of my favourite things is chocolate
       Another of my favourite things are videogames
       Another of my favourite things are holidays
       Another of my favourite things is relaxing
       These are 4 of my favourite things
'''

def favourite_things(*args):
    favourite_items= args
    for i,item in enumerate(favourite_items):
        if item.endswith("s"):
            verb="are"
        else:
            verb="is"
            
        if i==0:
            print(f"One of my favourite things {verb} {item}")  
        else :
            print(f"Another of my favourite things {verb} {item}")  
    print(f"These are {str(len(favourite_items))} of my favourite things")
        
favourite_things("chocolate","videogames","clothes")
