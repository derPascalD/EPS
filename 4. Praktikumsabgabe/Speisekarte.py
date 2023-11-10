speiseKarte = {"Schnitzel und Kroketten": 1500, "Burger und Steakhouse Pommes": 1650}
#python datei schreiben und lesen.

def speiseHinzufügen():
    print("Um die Aktion abzubrechen, drücken Sie nochmals 'n'.")

    print("Name des Gerichts:")
    nameEssen = (input())

    if nameEssen == "n":
        return

    print("Preis des Gerichts:")
    a = (input())

    try:
        
        int(a)
    except ValueError:
        if a == "n":
            ""
        else:
            print("Bitte nur Zahlen eingeben")
    preis = a

    if preis == "n":
        return

    speiseKarte.update({str(nameEssen): int(preis)})
    print("Gericht hinzugefügt!")

schleifeStarten = 0

while schleifeStarten != 1:
    print("\nHauptmenü:\n"
          "a = Speisekarte anzeigen lassen\n"
          "n = neues Gericht hinzufügen\n"
          "e = Programmende")
    userInput = input()
    if userInput == "a":

        print("Speisekarte: ")
        for i in speiseKarte:
            print(i + " - " + str(speiseKarte.get(i)) + " Cents")

    if userInput == "n":
        speiseHinzufügen()

    if userInput == "e":
        schleifeStarten = 1
