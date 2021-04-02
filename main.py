from os import system, name
from time import sleep
import random

class Utilities:
    def __init__(self):
        pass

    def screen_clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

class Scoreboard:
    def __init__(self):
        self.category_dict = {}
        self.number_of_lines = 0

        self.scoreboard_stage_one = []
        self.scoreboard_stage_two = []

        self.scoreboard_flag_one = False
        self.scoreboard_flag_two = False


def count_categories(Scrbrd):
    with open ("UnfinishedBusiness.txt", "r") as f:
        categories_all = []

        for lines in f:
            Scrbrd.number_of_lines += 1
            category = lines.split()[0]
            categories_all.append(category)

            if category not in Scrbrd.category_dict:
                Scrbrd.category_dict[category] = 1
            else:
                Scrbrd.category_dict[category] += 1

    print("Ladies and gentlemen.")
    sleep(1)
    print("You all know why we're here, so let's just get to it!")
    sleep(1)

    return Scrbrd


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ CATEGORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def roll_category(Scrbrd, Uti):
    roll = random.randrange(0, Scrbrd.number_of_lines)
    return find_category(roll, Scrbrd, Uti)


def find_category(roll, Scrbrd, Uti):
    for keys in Scrbrd.category_dict:

        if roll >= Scrbrd.category_dict[keys]:
            roll = roll - Scrbrd.category_dict[keys]
            continue

        else:
            category = keys
            break

    return add_category(Scrbrd, category, Uti)


def add_category(Scrbrd, category, Uti):
    Uti.screen_clear()

    if Scrbrd.scoreboard_flag_one == False:
        print("Randomly picked: " + category)
        sleep(0.5)

        if category not in Scrbrd.scoreboard_stage_one:
            Scrbrd.scoreboard_stage_one.append(category)
        else:
            Scrbrd.scoreboard_stage_two.append(category)
            Scrbrd.scoreboard_flag_one = True
            print("\nCurrent thing has 2 points:\n\n")

            print(category)
            sleep(0.5)

        if Scrbrd.scoreboard_flag_one == False:
            print("\nCurrent things have 1 point each:\n\n")

            for item in Scrbrd.scoreboard_stage_one:
                print(item, end="\n")

        sleep(0.5)

    else:
        print("Randomly picked: " + category)
        sleep(0.5)

        if category not in Scrbrd.scoreboard_stage_one:
            Scrbrd.scoreboard_stage_one.append(category)
        elif category not in Scrbrd.scoreboard_stage_two:
            Scrbrd.scoreboard_stage_two.append(category)
        else:
            Scrbrd.scoreboard_flag_two = True

        if Scrbrd.scoreboard_flag_two == False:
            print("\nCurrent things have 2 points each:\n\n")

            for item in Scrbrd.scoreboard_stage_two:
                print(item, end="\n")

        sleep(0.5)

    return Scrbrd, category


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ITEM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def save_elements(category):
    with open("UnfinishedBusiness.txt", "r") as f:
        elements = []

        for lines in f:
            if lines[0:len(category)] == category:
                elements.append(lines[len(category)+3:])

    return elements


def roll_element(elements, Uti, Scrbrd):
    roll = random.randrange(0, len(elements))
    return find_element(roll, elements, Uti, Scrbrd)


def find_element(roll, elements, Uti, Scrbrd):
    element = elements[roll]
    return add_element(element, Uti, Scrbrd)


def add_element(element, Uti, Scrbrd):
    Uti.screen_clear()

    if Scrbrd.scoreboard_flag_one == False:
        print("Randomly picked: " + element)
        sleep(0.5)

        if element not in Scrbrd.scoreboard_stage_one:
            Scrbrd.scoreboard_stage_one.append(element)
        else:
            Scrbrd.scoreboard_stage_two.append(element)
            Scrbrd.scoreboard_flag_one = True
            print("\nCurrent thing has 2 points:\n\n")

            print(element)
            sleep(0.5)

        if Scrbrd.scoreboard_flag_one == False:
            print("\nCurrent things have 1 point each:\n\n")

            for item in Scrbrd.scoreboard_stage_one:
                print(item, end="")

        sleep(0.5)

    else:
        print("Randomly picked: " + element)
        sleep(0.5)

        if element not in Scrbrd.scoreboard_stage_one:
            Scrbrd.scoreboard_stage_one.append(element)
        elif element not in Scrbrd.scoreboard_stage_two:
            Scrbrd.scoreboard_stage_two.append(element)
        else:
            Scrbrd.scoreboard_flag_two = True

        if Scrbrd.scoreboard_flag_two == False:
            print("\nCurrent things have 2 points each:\n\n")

            for item in Scrbrd.scoreboard_stage_two:
                print(item, end="\n")

        sleep(0.5)

    return Scrbrd, element


if __name__ == '__main__':
    Uti = Utilities()
    Scrbrd = Scoreboard()
    Uti.screen_clear()
    Scrbrd = count_categories(Scrbrd)

    # Choosing a category
    while True:
        Scrbrd, category = roll_category(Scrbrd, Uti)

        if Scrbrd.scoreboard_flag_two == True:
            print(category, "is the winning category!\n")
            sleep(2)
            break

    # Picking from within category

    Scrbrd = Scoreboard()
    list_of_elements = save_elements(category)

    while True:
        Scrbrd, element = roll_element(list_of_elements, Uti, Scrbrd)

        if Scrbrd.scoreboard_flag_two == True:
            print(element, "is the winner!!!")
            sleep(5)
            break