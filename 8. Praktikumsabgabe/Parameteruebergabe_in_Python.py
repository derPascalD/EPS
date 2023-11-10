intZahl = 21
stringName = "Pascal"
liste = ["Pascal", 21]


def test_call_by_value_or_reference(test):
    """Hier wird eine vorhandene Variable in der Funktion geändert"""
    test = 100
    print("In der Funktion: " + str(test))


def listenelement_veraendern(liste):
    """Hier wird einer vorhandenen Liste ein Element verändert"""
    liste[1] = 100
    for i in liste:
        print("In der Funktion: " + str(i))


def listenekomplett_veraendern(list):
    """Hier wird eine vorhandene Liste überschrieben"""
    list2 = ["Daniel", 21]
    list = list2
    for i in list:
        print("In der Funktion: " + str(i))


# Call by Value
print("CallbyValueOrReference")
print("IntZahl Vorher: " + str(intZahl))
test_call_by_value_or_reference(intZahl)
print("IntZahl Nacher: " + str(intZahl))

# Call by Value
print("\nCallbyValueOrReference")
print("StringName: " + stringName)
test_call_by_value_or_reference(stringName)
print("StringName: " + stringName)

# Cal by Reference
print("\nCallbyValueOrReference Test 1")
for i in liste:
    print("ListeStrings Inhalt Vorher: " + str(i))
listenelement_veraendern(liste)
for i in liste:
    print("ListeStrings Inhalt Nacher: " + str(i))

    # Cal by Value
print("\nCallbyValueOrReference Test 2")
for i in liste:
    print("ListeStrings Inhalt Vorher: " + str(i))
listenekomplett_veraendern(liste)
for i in liste:
    print("ListeStrings Inhalt Nacher: " + str(i))
