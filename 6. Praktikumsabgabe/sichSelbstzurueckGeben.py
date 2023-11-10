print("Hallo, ich gebe mich selbst zurück!")
programm = [""]

with open('sichSelbstzurueckGeben.py') as a:
    for line in a:
        programm.append(line)

for line in programm:
    print(line)

