speisekarte = dict()
liste = []

try:
    datei = open('speisekarte.txt', 'r')

except:
    datei = open('speisekarte.txt', 'w')
    datei.write("Test, 1")
    datei.close()
    datei = open('speisekarte.txt', 'r')

for zeile in datei:
    temp = zeile.replace("\n", "")
    item = temp.split(", ")
    speisekarte.update({item[0]: item[1]})
    liste.append(item[0])
datei.close()


def speisenanzeigen(speisekarte_uebergabe):
    print("Speisekarte: ")
    for i in speisekarte_uebergabe:
        print(i + " - " + str(speisekarte_uebergabe.get(i)) + " Cents")
    return speisekarte_uebergabe


def speise_hinzufuegen(speisekarte_uebergabe):
    print("Um die Aktion abzubrechen, drücken Sie nochmals 'n'.")

    print("Name des Gerichts:")

    try:
        nameEssen = str(input())
    except ValueError:
        print("Keine gueltige Eingabe")
        return speisekarte

    if nameEssen == "n":
        return speisekarte

    print("Preis des Gerichts:")

    a = input()
    try:
        int(a)
        if a == "":
            return speisekarte
    except ValueError:
        print("Bitte nur Zahlen eingeben")
        return speisekarte
    preis = a

    if preis == "n":
        return speisekarte

    speisekarte_uebergabe.update({str(nameEssen): int(preis)})

    print("Gericht hinzugefügt!")
    return speisekarte_uebergabe


def speise_loeschen(speisekarte_uebergabe):
    counter = 0

    print("Speisekarte: ")
    for j in speisekarte_uebergabe:
        counter += 1
        print(str(counter) + ". " + j + " - " + str(speisekarte_uebergabe.get(j)) + " Cents")

    print("Welches gericht wollen sie loeschen?")

    try:
        eingabe = int(input())
        int(eingabe)
    except ValueError:
        print("Keine gueltige Eingabe")
        return

    if len(liste) < eingabe:
        print("Bitte nur Zahlen eingeben die vorhanden sind.")
    else:
        gericht = liste[eingabe - 1]
        speisekarte_uebergabe.pop(gericht)
        liste.pop(eingabe - 1)
        print(gericht + " entfernt!")

    return speisekarte_uebergabe


def programm_ende(speisekarte_uebergab):
    datei1 = open('speisekarte.txt', 'w')

    for i in speisekarte_uebergab:
        datei1.write(i + ", " + str(speisekarte_uebergab.get(i)) + "\n")
    datei1.close()
    return 1


start_ende = 0

while start_ende != 1:
    print("\nHauptmenü:\n"
          "a = Speisekarte anzeigen lassen\n"
          "n = neues Gericht hinzufuegen\n"
          "e = Programmende\n"
          "l = Gericht loeschen\n")

    userInput = input()
    if userInput == "a":
        speisekarte = speisenanzeigen(speisekarte)

    if userInput == "n":
        speisekarte = speise_hinzufuegen(speisekarte)

    if userInput == "l":
        speisekarte = speise_loeschen(speisekarte)

    if userInput == "e":
        start_ende = programm_ende(speisekarte)
