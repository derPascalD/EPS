speisekarte = dict()
liste = []
kategorie = []

try:
    datei = open('speisekarte.txt', 'r')

except IOError or FileNotFoundError:
    print("Datei kann nicht geöffnet werden oder existiert nicht.")
    exit()

for zeile in datei:
    temp = zeile.replace("\n", "")
    item = temp.split(", ")
    speisekarte.update({item[0]: item[1]})

    liste.append(item[0])
    kategorie.append(item[2])

datei.close()


def speisenanzeigen(speisekarte_uebergabe):
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

    print("Kategorien:")
    print("Zur Auswahl stehen:\n1. Vorspeise\n2. Hauptspeise\n3. Nachspeise\n4. Getraenk\n")
    print("Bitte geben sie für die Kategorie die Nummer ein!")

    while 1:
        b = input()
        if b == "":
            return speisekarte_uebergabe

        elif b == str(1):
            liste.append(nameEssen)
            kategorie.append("Vorspeise")
            speisekarte_uebergabe.update({str(nameEssen): int(preis)})
            print("Gericht hinzugefügt!")
            return speisekarte_uebergabe

        elif b == str(2):
            liste.append(nameEssen)
            kategorie.append('Hauptspeise')
            speisekarte_uebergabe.update({str(nameEssen): int(preis)})
            print("Gericht hinzugefügt!")
            return speisekarte_uebergabe

        elif b == str(3):
            liste.append(nameEssen)
            kategorie.append('Nachspeise')
            speisekarte_uebergabe.update({str(nameEssen): int(preis)})
            print("Gericht hinzugefügt!")

            return speisekarte_uebergabe
        elif b == str(4):
            liste.append(nameEssen)
            kategorie.append('Getraenk')
            speisekarte_uebergabe.update({str(nameEssen): int(preis)})
            print("Gericht hinzugefügt!")
            return speisekarte_uebergabe
        else:
            print("Kategorie gibt es nicht!")


def speise_loeschen(speisekarte_uebergabe):
    counter = 0

    print("Speisekarte: ")
    for j in speisekarte_uebergabe:
        counter += 1
        print(str(counter) +  ". " + j + " - " + str(speisekarte_uebergabe.get(j)) + " Cents" + " - " +
              kategorie[counter - 1])

    print("Welches Gericht wollen sie loeschen?")

    eingabe = input()
    if eingabe == "":
        return speisekarte_uebergabe
    else:
        try:
            eingabe = int(eingabe)
        except ValueError:
            print("Keine gueltige Eingabe")
            return speisekarte_uebergabe

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


def speisekarte_aendern(speisekarte_uebergabe):
    preisListe = []
    kategorie2 = kategorie
    counter = 0
    print("Speisekarte: ")
    for j in speisekarte_uebergabe:
        counter += 1
        print(str(counter) + ". " + j + " - " + str(speisekarte_uebergabe.get(j)) + " Cents" + " - " + kategorie[
            counter - 1])
        preisListe.append(speisekarte_uebergabe.get(j))

    print("Welches Gericht wollen sie aendern?")
    eingabe = input()

    if eingabe == "":
        return speisekarte_uebergabe
    else:
        try:
            eingabe = int(eingabe)
        except ValueError:
            print("Keine gueltige Eingabe")
            return speisekarte_uebergabe
    if eingabe < 1:
        print("Zahl gibt es nicht!")
    else:
        if len(liste) < eingabe:
            print("Bitte nur Zahlen eingeben die vorhanden sind.")
        elif eingabe == "":
            return speisekarte_uebergabe
        else:
            gericht = liste[int(eingabe) - 1]
            preis = preisListe[int(eingabe) - 1]
            kategorie3 = kategorie2[int(eingabe) - 1]
            print("Gericht: " + gericht)
            print("Preis: " + str(preis))
            print("Kategorie: " + kategorie3)

            print("Was wollen sie ändern?")
            print("1. Gericht\n2. Preis\n3. Kategorie")
            eingabe2 = input()
            if eingabe2 == str(1):
                print("Bitte geben Sie einen neuen Namen ein!")
                gerichtGeaendert = input()
                if gerichtGeaendert == "":
                    return speisekarte_uebergabe
                else:
                    speisekarte_uebergabe.pop(liste[eingabe - 1])
                    liste.pop(eingabe - 1)
                    kategorie.pop(eingabe - 1)
                    liste.append(gerichtGeaendert)
                    kategorie.append(kategorie3)
                    speisekarte_uebergabe.update({str(gerichtGeaendert): int(preis)})
                    print(gericht + " geändert zu " + gerichtGeaendert + ".")
            elif eingabe2 == "":
                return speisekarte_uebergabe
            elif eingabe2 == str(2):
                print("Bitte geben Sie einen neuen Preis ein!")
                while 1:
                    neuerPreis = input()
                    if neuerPreis == "":
                        return speisekarte_uebergabe
                    try:
                        int(neuerPreis)
                    except ValueError:
                        print("Bitte nur Zahlen eingeben.")
                        print("Bitte erneut versuchen")
                        pass
                    else:
                        speisekarte_uebergabe[liste[int(eingabe) - 1]] = neuerPreis
                        print("Neuer Preis ist " + str(neuerPreis) + ".")
                        return speisekarte_uebergabe
            elif eingabe2 == str(3):
                print("Bitte geben Sie eine neue Kategorie ein!")
                print("Zur Auswahl stehen:\n1. Vorspeise\n2. Hauptspeise\n3. Nachspeise\n4. Getraenk\n")
                print("Bitte geben sie für die Kategorie die Nummer ein!")

                while 1:
                    neueKategorie = input()
                    if neueKategorie == "":
                        return speisekarte_uebergabe

                    elif neueKategorie == str(1):
                        speisekarte_uebergabe.pop(liste[eingabe - 1])
                        liste.pop(eingabe - 1)
                        kategorie.pop(eingabe - 1)
                        liste.append(gericht)
                        kategorie.append("Vorspeise")
                        speisekarte_uebergabe.update({str(gericht): int(preis)})
                        print(kategorie3 + " geändert zu " + "Vorspeise.")
                        return speisekarte_uebergabe
                    elif neueKategorie == str(2):
                        speisekarte_uebergabe.pop(liste[eingabe - 1])
                        liste.pop(eingabe - 1)
                        kategorie.pop(eingabe - 1)
                        liste.append(gericht)
                        kategorie.append("Hauptspeise")
                        speisekarte_uebergabe.update({str(gericht): int(preis)})
                        print(kategorie3 + " geändert zu " + "Hauptspeise.")
                        return speisekarte_uebergabe
                    elif neueKategorie == str(3):
                        speisekarte_uebergabe.pop(liste[eingabe - 1])
                        liste.pop(eingabe - 1)
                        kategorie.pop(eingabe - 1)
                        liste.append(gericht)
                        kategorie.append("Nachspeise")
                        speisekarte_uebergabe.update({str(gericht): int(preis)})
                        print(kategorie3 + " geändert zu " + "Nachspeise.")
                        return speisekarte_uebergabe
                    elif neueKategorie == str(4):
                        speisekarte_uebergabe.pop(liste[eingabe - 1])
                        liste.pop(eingabe - 1)
                        kategorie.pop(eingabe - 1)
                        liste.append(gericht)
                        kategorie.append("Getraenk")
                        speisekarte_uebergabe.update({str(gericht): int(preis)})
                        print(kategorie3 + " geändert zu " + "Getraenk.")
                        return speisekarte_uebergabe
                    else:
                        print("Kategorie gibt es nicht!")
                        print("Bitte erneut versuchen")
            else:
                print("Bitte keine Buchstaben oder falsche Zahlen eintragen")
    return speisekarte_uebergabe


def programm_ende(speisekarte_uebergabe):
    counter = 0

    try:
        datei1 = open('speisekarte.txt', 'w')
    except IOError or FileNotFoundError:
        print("Datei nicht gefunden oder konnte nicht aufgerufen werden1")
        exit()

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
          "l = Gericht loeschen\n"
          "s = Gericht aendern\n")

    userInput = input()
    if userInput == "a":
        speisekarte = speisenanzeigen(speisekarte)

    if userInput == "n":
        speisekarte = speise_hinzufuegen(speisekarte)

    if userInput == "s":
        speisekarte_aendern(speisekarte)

    if userInput == "l":
        speisekarte = speise_loeschen(speisekarte)

    if userInput == "e":
        start_ende = programm_ende(speisekarte)
