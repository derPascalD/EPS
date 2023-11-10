# x wurde in der Parameterübergabe schon gesetzt,
# um fehler zu vermeiden
def defaulparameter(x=None):
    print(x)


# Aufruf der Funktion
defaulparameter()


# Die Werte für die Variablen werden Positionsabhängig übergeben.
def positionsparameter(var1, var2):
    print(var2 + var1)


# Übergabe der Parameter, Reihenfolge wird beachtet
positionsparameter("Pascal", " Daniel")
positionsparameter("5", " 4")


# Übergabe der Variablen die Werte vorher zugewiesen wurde
def benannteparameter(eins, zwei):
    print(eins / zwei)


# Variablen werden direkt zugewiesen und an welcher Stelle ist egal
benannteparameter(zwei=2, eins=1)
benannteparameter(eins=1, zwei=2)

# Werte die zusammengepackt wurden und abgespeichert wurde in "zusammengepackt".
zusammengepackt = ["Ich ", "heiße ", "Pascal."]


# unpacking
def auspacken(x, y, z):
    print(x + y + z)

# Aufruf der Funktion
auspacken(*zusammengepackt)


# packing
def verpacken(*args):
    zahl = 2
    zahl = zahl * sum(args)
    print(zahl)


# Aufruf der Funktion
verpacken(1, 2, 3)


# Methode wo der Inhalt des Dictionary übergeben wird
def ausgabeDict(vorname, nachname):
    print(vorname, nachname)


# füllen des Dictionary
dictonary = {"vorname""": "Pascal", "nachname": "Daniel"}

# auspacken des Dictionary
ausgabeDict(**dictonary)
