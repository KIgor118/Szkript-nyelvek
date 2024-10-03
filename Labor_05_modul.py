def felhasznalnev():
    _felhnev = input("Adja meg a felhasználó nevét (email cím): ")
    while " " in _felhnev or not "@" in _felhnev or not "." in _felhnev:
        print("Érvénytelen email formátum!")
        if " " in _felhnev:
            print("A felhasználónév szóközt tartalmaz!")
        if "@" not in _felhnev:
            print("A felhasználónév nem tartlamaz @ jelet!")
        if "." not in _felhnev:
            print("A felhasznalóneév nem tartlamaz . jelet")
        _felhnev = input("Adja meg a felhasználó nevét (email cím)2: ")
    return _felhnev

#-----------------------------------------------------------------------------------------------------------------------

def jelszo_bekerese(hossz):
    def jsz_hossza(_jelszo,_hossz):
        ok = True
        if len(_jelszo) < _hossz:
            ok = False
        return ok

    def szam(_jelszo):
        ok = False
        for betu in _jelszo:
            if betu.isnumeric():
                ok = True
        return ok


    def kisbetu(_jelszo):
        ok = False
        for betu in _jelszo:
            if betu.islower():
                ok = True
        return ok


    def nagybetu(_jelszo):
        ok = False
        for betu in _jelszo:
            if betu.isupper():
                ok = True
        return ok

    jelszo = input("Adja meg a jelszavát: ")
    while not jsz_hossza(jelszo,hossz) or not szam(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo):
        print("Rossz a jelszó!")
        jelszo = input("Adja meg a jelszavát: ")
    return jelszo

#-----------------------------------------------------------------------------------------------------------------------

