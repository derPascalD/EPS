def hoch(x, i):
    if i == 0:
        return 1
    else:
        return x * hoch(x, i - 1)


print("Willkommen bei Potenzen berechnen")
ende = 1
while ende:
    print("Bitte geben Sie zuerst die Basis. Bei Enter wird die Basis auf 2 gesetzt!")
    x = input()
    print("Bitte geben den Exponenten ein.")
    i = input()
    if x == "":
        x = 2
    try:
        x = int(x)
        i = int(i)
        ende = 0
    except ValueError:
        print("Bitte nur Zahlen eintragen!")
print(hoch(x, i))
