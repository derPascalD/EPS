wort = "test wort"


def scopes():
    """
    Hier sind weitere Funktionen drin und
    hier wird die Scope Variable ausgegeben.
    """
    wort = "scopes wort"

    def do_local():
        """
        Hier wird die Lokale Variable ausgegeben
        """
        wort = "local wort"
        print("in do_local: " + wort)

    def do_nonlocal():
        """
        Hier wird die nicht Lokale Variable ausgegeben, nur die in der Funktion
        """
        nonlocal wort
        wort = "nonlocal wort"
        print("in do_nonlocal: " + wort)

    def do_global():
        """
        Hier wird globale Variable ausgegeben und geändert
        """
        global wort
        wort = "global wort"
        print("in do_global: " + wort)

    for i in range(1, 5):
        print("in scopes: " + wort)
        if i == 1:
            do_local()
        if i == 2:
            do_nonlocal()
        if i == 3:
            do_global()


for i in range(1, 4):
    if i == 1 or i == 3:
        print("im Hauptprogramm: " + wort)
    else:
        scopes()
