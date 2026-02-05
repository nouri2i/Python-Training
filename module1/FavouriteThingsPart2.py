'''
Docstring for module1.FavouriteThingsPart2
Let's refine our favourite things list. We'll rank some of our favourite things, and mention some others that we didn't rank among the best.

You can have a top 3, top 5 or however many you like!

Using what you've learned about *args and **kwargs, write a function that looks like this:

  favourite_things(other_item1, other_item2, etc..., First=top_item, Second=2nd_item, etc....) 
That returns a ranking of your favourite things, along with some others that didn't make the ranking. Make sure to tell us wether it is a top 3, top 5 or however many you chose.

'''

def favourite_things(*args,**kwargs):
    top_favourites =kwargs
    other_favourites = args
    print(f"Here are my top {str(len(top_favourites))} favourite things /n")  
    print("-------------")

    for postion,top_item in top_favourites.items():
        print(f"{postion} : {top_item}")
    print("-------------")
    print("Some of my other favourite things are: ")

    for index, other_item in enumerate(other_favourites):
        if index ==len(other_favourites)-1:
            print(f"and {other_item} " )
        else:
            print(f"{other_item} ")
       
favourite_things("chocolate","videogames","clothes",First="Football",Second="Judo",Third="Sweeming")
