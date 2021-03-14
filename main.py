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
        self.scoreboard_stage_one = []
        self.scoreboard_stage_two = []

        self.scoreboard_flag_one = False
        self.scoreboard_flag_two = False


def Count_Lines():
    with open("UnfinishedBusiness.txt", "r") as f:
        print("Ladies and gentlemen.")
        sleep(1)
        print("You all know why we're here, so let's just get to it!")
        sleep(1)
        list_of_lines = f.readlines()
        uniqueEntries = len(list_of_lines)
        return uniqueEntries

def Randomize_Number(maxNum):
    roll = random.randrange(0, maxNum)
    return roll

def Find_The_Line(lineNumber):
    with open("UnfinishedBusiness.txt", "r") as f:
        another_list_of_lines = f.readlines()
        chosenThing = another_list_of_lines[lineNumber]
        return chosenThing

def First_To_Three(Uti, Scoreboard, chosenThing):
    Uti.screen_clear()

    if Scoreboard.scoreboard_flag_one == False:
        print("Randomly picked: " + chosenThing)
        sleep(0.1)

        if chosenThing not in Scoreboard.scoreboard_stage_one:
            Scoreboard.scoreboard_stage_one.append(chosenThing)
        else:
            Scoreboard.scoreboard_stage_two.append(chosenThing)
            Scoreboard.scoreboard_flag_one = True

            print("\nCurrent thing has 2 points:\n\n")

            print(chosenThing)
            sleep(0.1)

        if Scoreboard.scoreboard_flag_one == False:
            print("\nCurrent things have 1 point each:\n\n")

            for item in Scoreboard.scoreboard_stage_one:
                print(item, end="")

        sleep(2)

    else:
        print("Randomly picked: " + chosenThing)
        sleep(0.1)

        if chosenThing not in Scoreboard.scoreboard_stage_one:
            Scoreboard.scoreboard_stage_one.append(chosenThing)
        elif chosenThing not in Scoreboard.scoreboard_stage_two:
            Scoreboard.scoreboard_stage_two.append(chosenThing)
        else:
            Scoreboard.scoreboard_flag_two = True

        if Scoreboard.scoreboard_flag_two == False:
            print("\nCurrent things have 2 points each:\n\n")

            for item in Scoreboard.scoreboard_stage_two:
                print(item, end="")

        sleep(2)


if __name__ == '__main__':
    Uti = Utilities()
    Scrbrd = Scoreboard()
    Uti.screen_clear()
    lines = Count_Lines()

    while True:
        randomNumber = Randomize_Number(lines)
        chosenThing = Find_The_Line(randomNumber)
        First_To_Three(Uti, Scrbrd, chosenThing)

        if Scrbrd.scoreboard_flag_two == True:
            print(chosenThing, " is the winner!")
            break
