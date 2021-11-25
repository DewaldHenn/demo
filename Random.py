import random

def Main():
    RandomNumber()
    RandomNames()
    RandomSingle()

def RandomNumber():

    num_list = [6,7,8,9,10,11,12]
    print("List before using shuffle: ",num_list)

    random.shuffle(num_list)
    print("List after using shuffle method: ",num_list)

def RandomNames():

    name_list = ["Dewald", "Christiaan", "Dillon", "Zubair"]
    print("List before using shuffle: ", name_list)

    random.shuffle(name_list)
    print("List after using shuffle method: ", name_list)

def RandomSingle():

    colours_list = ["Black", "Blue", "Purple", "Green"]
    x = len(colours_list) - 1
    print(x)
    print("List before using randint: ", colours_list)

    print("List after using randit method: ", colours_list[random.randint(0,x)])

Main()