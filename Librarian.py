chapters = [
    "Down the Rabbit-Hole",
    "The Pool of Tears",
    "A Caucus-Race and a Long Tale",
    "The Rabbit Sends in a Little Bill",
    "Advice from a Caterpillar"
]
''''
i = 1
for chapter in chapters:
    i+=1
    print(f"{i}: {chapter}")
    '''

for index,chapter in enumerate(chapters):
    print(f"{index+1}: {chapter}")