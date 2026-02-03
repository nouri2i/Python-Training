## Task:
'''
You are a scientist known across the land for creating the best and most powerful superheros.
It's another day at the lab and you now have all the tools to create the ultimate superhero.

- Create a class for your superhero and define its stats for strength, speed and whether it can fly or not

- Create a function perform_ability() that defines what happens when your hero uses their special power

- Create an instance of the class to make the hero come to life

## Extra practice:

- Feel free to add as many abilities to your hero as you like and create multiple heros to practice inheritance
'''

class HeroFactory:
    def __init__(self,name, strength,speed,fly):
        self.name=name
        self.strength=strength
        self.speed=speed
        self.fly=fly

    def perform_ability(self):
        able_to_fly=" and is able to fly."
        ability=f"{self.name} has a  strength of {self.strength} horsepower his speed is {self.speed}"
        if self.fly==True:
            ability+=able_to_fly
        print(ability)

HeroFactory("Hulk",100, 300, True).perform_ability()