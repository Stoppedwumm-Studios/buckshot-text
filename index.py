
from random import randint
from os import system
import keras
items = ["beer", "saw", "cigarettes", "magnifying glass", "handcuffs"]
gun = []

def GenerateItems():
    if True:
        for p in range(2):
            pitems = []
            for count in range(6):
                pitems.append(items[randint(0, len(items) - 1)])
            print(pitems)

while True:
    action = input("(items,gun,insert,shoot,clearo) ")
    
    if action == "items":
        GenerateItems()
    elif action == "gun":
        print(gun)
    elif action == "insert":
        empty = int(input("Number of empty rounds: "))
        live = int(input("Number of live rounds: "))
        allrounds = empty + live
        percent = live / allrounds * 100
        print("Chance of death: " + str(percent) + "%")
        for round in range(allrounds):
            roundvalue = input("Live or blank? ")
            gun.append(roundvalue)
    elif action == "shoot":
        print("Was " + gun[0])
        gun.__delitem__(0)
        print(gun)
    elif action == "clearo":
        system("cls")