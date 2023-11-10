speisekarte = dict()
liste = []
kategorie = []

try:
    datei = open('speisekarte.txt', 'r')

except:
    datei = open('speisekartetest.txt', 'w')
    datei.write("Test, 1, test")
    datei.close()
    datei = open('speisekartetest.txt', 'r')

for zeile in datei:
    temp = zeile.replace("\n", "")
    item = temp.split(", ")
    speisekarte.update({item[0]: item[1]})

    liste.append(item[0])
    kategorie.append(item[2])

datei.close()


def speisenanzeigen( speisekarte_uebergabe):
    counter = -1
    print("//Speisekarte// \n")
    print("Vorspeise:")
    for i in speisekarte_uebergabe:
        counter += 1
        if kategorie[counter] == "Vorspeise":
            print(i + " - " + str(speisekarte_uebergabe.get(i)) + " Cents")
    counter = -1
    print("\nHauptspeise:")
    for i in speisekarte_uebergabe:
        counter += 1
        if kategorie[counter] == "Hauptspeise":
            print(i + " - " + str(speisekarte_uebergabe.get(i)) + " Cents")
    counter = -1
    print("\nNachspeise:")
    for i in speisekarte_uebergabe:
        counter += 1
        if kategorie[counter] == "Nachspeise":
            print(i + " - " + str(speisekarte_uebergabe.get(i)) + " Cents")
    counter = -1
    print("\nGetraenk:")
    for i in speisekarte_uebergabe:
        counter += 1
        if kategorie[counter] == "Getraenk":
            print(i + " - " + str(speisekarte_uebergabe.get(i)) + " Cents")

    return speisekarte_uebergabe

def speise_hinzufuegen(speisekarte_uebergabe):
    print("Um die Aktion abzubrechen, drücke 'Enter'.")

    print("Name des Gerichts:")

    try:
        nameEssen = str(input())
        if nameEssen == "":
            return speisekarte_uebergabe
    except ValueError:
        print("Keine gueltige Eingabe")
        return speisekarte_uebergabe

    print("Preis des Gerichts:")

    a = input()
    if a == "":
        return speisekarte_uebergabe

    try:
        int(a)
    except ValueError:
        print("Bitte nur Zahlen eingeben.")
        return speisekarte_uebergabe
    preis = a

    print("Kategorie:")
    print("Zur Auswahl stehen: Vorspeise, Hauptspeise, Nachspeise und Getraenk.")
    b = input()
    if b == "":
        return speisekarte_uebergabe

    elif b == "Vorspeise":
        liste.append(nameEssen)
        kategorie.append(b)
        speisekarte_uebergabe.update({str(nameEssen): int(preis)})
        print("Gericht hinzugefügt!")
        return speisekarte_uebergabe
    elif b == 'Hauptspeise':
        liste.append(nameEssen)
        kategorie.append(b)
        speisekarte_uebergabe.update({str(nameEssen): int(preis)})
        print("Gericht hinzugefügt!")
        return speisekarte_uebergabe
    elif b == 'Nachspeise':
        liste.append(nameEssen)
        kategorie.append(b)
        speisekarte_uebergabe.update({str(nameEssen): int(preis)})
        print("Gericht hinzugefügt!")
        return speisekarte_uebergabe
    elif b == 'Getraenk':
        liste.append(nameEssen)
        kategorie.append(b)
        speisekarte_uebergabe.update({str(nameEssen): int(preis)})
        print("Gericht hinzugefügt!")
        return speisekarte_uebergabe
    else:
        print("Kategorie gibt es nicht!")
        return speisekarte_uebergabe


def speise_loeschen(speisekarte_uebergabe):
    counter = 0

    print("Speisekarte: ")
    for j in speisekarte_uebergabe:
        counter += 1
        print(str(counter) + ". " + j + " - " + str(speisekarte_uebergabe.get(j)) + " Cents" + " - " + kategorie[
            counter - 1])

    print("Welches gericht wollen sie loeschen?")

    eingabe = input()
    if eingabe == "":
        return speisekarte
    else:
        try:
            eingabe = int(eingabe)
        except ValueError:
            print("Keine gueltige Eingabe")
            return speisekarte

    if eingabe < 1:
        print("Zahl gibt es nicht!")
    else:
        if len(liste) < eingabe:
            print("Bitte nur Zahlen eingeben die vorhanden sind.")
        else:
            gericht = liste[eingabe - 1]
            speisekarte_uebergabe.pop(gericht)
            liste.pop(eingabe - 1)
            kategorie.pop(eingabe - 1)
            print(gericht + " entfernt!")

    return speisekarte_uebergabe


def programm_ende(speisekarte_uebergabe):
    counter = 0
    datei1 = open('speisekarte.txt', 'w')

    for i in speisekarte_uebergabe:
        datei1.write(i + ", " + str(speisekarte_uebergabe.get(i)) + ", " + kategorie[counter] + "\n")
        counter += 1
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
