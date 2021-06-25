import random

counter = 0

print("\n")

Runden = 0
while Runden == 0:
    try:
        Runden = int(input("Wie viele Runden magst du spielen?  "))
    except:
        continue

while counter < Runden:
    mensch = input("Schere, Stein oder Papier?  ").lower()

    möglichkeiten = ["schere", "stein", "papier"]

    computer = random.choice(möglichkeiten)

    print("Wahl vom Computer:", computer)


    if mensch == "schere" and computer == "papier":
        print("---> Du hast gewonnen!")
    elif mensch == "papier" and computer == "stein":
        print("---> Du hast gewonnen!")
    elif mensch == "stein" and computer == "schere":
        print("---> Du hast gewonnen!")

    elif mensch == "schere" and computer == "stein":
        print("---> Du hast verloren!")
    elif mensch == "papier" and computer == "schere":
        print("---> Du hast verloren!")
    elif mensch == "stein" and computer == "papier":
        print("---> Du hast verloren!")

    elif mensch == "schere" and computer == "schere":
        print("---> Unentschieden!")
    elif mensch == "papier" and computer == "papier":
        print("---> Unentschieden!")
    elif mensch == "stein" and computer == "stein":
        print("---> Unentschieden!")

    else:
        print("---> Falscheingabe")
    
    counter = counter + 1

print("\n")

#test