def adatok_bekerese():
    jel = input("Adja meg a müveleti jelet(+,-,*,/): ")
    while jel not in ("+", "-", "*", "/"):
        print("Nem megfelelő input\nKérek másikat")
        jel = input("Adja meg a müveleti jelet(+,-,*,/): ")

    elso = input("Egyik szám: ")
    while not elso.isnumeric():
        print("Nem megfelelő input\nKérek másikat")
        elso = input("Egyik szám: ")
    elso = int(elso)

    masodik= input("Másik szám: ")
    while not masodik.isnumeric():
        print("Nem megfelelő input\nKérek másikat")
        masodik = input("Másik szám: ")
    masodik = int(masodik)

    return jel, elso, masodik

def muveletek_vegrehajtasa(jel, elso, masodik):
    if jel == "+":
        muvelet = elso + masodik
    elif jel == "-":
        muvelet = elso - masodik
    elif jel == "*":
        muvelet = elso * masodik
    elif jel == "/":
        muvelet = elso / masodik

    return muvelet

def eredmenyek_megjelenitese(jel, elso, masodik, muvelet):
    print(elso,jel,masodik,"=",muvelet)
    return