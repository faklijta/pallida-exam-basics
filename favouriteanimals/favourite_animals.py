# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys

def get_args():
    return sys.argv


def add_animals(animal):
    with open("favourites.txt", "a") as file:
        file.write(str(animal) + '\n')


def read_file(file):
    with open(file) as f:
        return f.read()


def check_if_listed(file):
    animals_list = read_file(file).split()
    pass


def controller():
    arguments = get_args()
    if len(arguments) == 1:
        print("Usage:\n ```fav_animals [animal] [animal]```")
    elif len(arguments) >= 2:
        add_animals(sys.argv[1:])


controller()