import random
import sys

#Falscheingaben möglich machen
def zahl_einlesen(text, min, max):
    while True:
        try:
            zahl = int(input(text))
            if zahl < min or zahl > max:
                print("-> ungültige Eingabe!")
                continue
            return zahl
        except:
            print("-> ungültige Eingabe!")

user = 0
pc = 0
Runden = 0

print("\n")
print("=================================================")
print("\t\tSCHERE STEIN PAPIER")
print("=================================================")

#Spiel laden
fortsetzung = input("Willst du ein Spiel laden? (Für JA -> Y eingeben)").lower()

if fortsetzung == "y":
    with open("safegame.txt", "r") as letzstand:
        zeile = letzstand.readline()
        werte = zeile.split(" ") 
        user = int(werte[0])
        pc = int(werte[1])
        Runden = int(werte[2])
else:
    Runden = zahl_einlesen("Wie viele Runden willst du spielen? ",1, 100)


print("Entscheide Dich! Schere, Stein oder Papier")                         
print("-------------------------------------------------")


schere = 1
stein = 2
papier = 3

for i in range(Runden):

    print("\n")
    Eingabe_Nutzer = zahl_einlesen("Ihre Wahl: \n 1 Schere \t 2 Stein \t 3 Papier \n 0 Spiel speichern \n-> ",0,3)

#Spiel speichern
    if Eingabe_Nutzer == 0:
        with open("safegame.txt", "w") as letzstand:
            letzstand.write(f"{user} {pc} {Runden - i}")
            sys.exit()

#Auswahl Symbol
    if Eingabe_Nutzer == schere or Eingabe_Nutzer == stein or Eingabe_Nutzer == papier:
        Wert = random.randint(0, 2)
        Eingabe_Computer = ""
        if Wert == 0:
            Eingabe_Computer = schere
            print("-> Computer Wahl: Schere")
        elif Wert == 1:
            Eingabe_Computer = stein
            print("-> Computer Wahl: Stein")
        elif Wert == 2:
            Eingabe_Computer = papier
            print("-> Computer Wahl: Papier")


#Entscheidung und Ausgabe Zwischenergebnis
        if Eingabe_Nutzer == schere and Eingabe_Computer == papier:
            print("===> Glückwunsch! Schere schneidet Papier")
            user += 1
            print("\n")
        elif Eingabe_Nutzer == stein and Eingabe_Computer == schere:
            print("===> Glückwunsch! Stein schlägt Schere")
            user += 1
            print("\n")
        elif Eingabe_Nutzer == papier and Eingabe_Computer == stein:
            print("===> Glückwunsch! Papier schlägt Stein")
            user += 1
            print("\n")
        elif Eingabe_Nutzer == Eingabe_Computer:
            print("===> Unentschieden Nochmal!")
            print("\n")
        else:
            print("===> Schade!" , Eingabe_Computer, "schlägt", Eingabe_Nutzer)
            pc += 1

    else:
        print("--> Ihre Eingabe ist nicht gültig")


    print("-------------------------------------------------")

#Ausgabe Endergebnis
print("Ergebnis: \nComputer: {} \t Du: {} \n".format (pc ,user))

if user < pc:
    print("Du hast verloren! ")
elif user > pc:
    print("Du hast gewonnen! ")
else:
    print("Unentschieden")

    
print("=================================================")
print("\n")