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


def jelszo_ellenorzese(jelszo):
    ok = True
    prob = 0
    while True:
        jelszo2 = input("Kérem megint a jelszót: ")
        if jelszo == jelszo2:
            break
        else:
            prob += 1
            if prob == 3:
                ok = False
                break
            print("Nem azonos a két jelszó! Próbálja újra!")
    return ok

    def rogzit(nev, jsz):
        with open('adatok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(nev + ";" + jsz + "\n")


def regisztracio():
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

        _jelszo = input("Adja meg a jelszavát: ")
        while not jsz_hossza(_jelszo,hossz) or not szam(_jelszo) or not kisbetu(_jelszo) or not nagybetu(_jelszo):
            print("Rossz a jelszó!")
            _jelszo = input("Adja meg a jelszavát: ")
        return _jelszo

        felhnev = felhasznalnev()
        jelszo =  jelszo_bekerese(8)
        ok = jelszo_ellenorzese(jelszo)
        if ok:
            rogzit(felhnev, jelszo)
        return ok


def beleptetes():
    def felhbeker():
        jelszo = False
        email = felhasznalnev()
        with open("adatok.txt","r",encoding="utf-8") as falj:
            for sor in falj:
                felhasznalo = sor.strip().split(";")
                if felhasznalo[0] == email:
                    jelszo = felhasznalo[1]
                    break
        return jelszo
    felhasznalo = felhbeker()
    if not felhasznalo:
        print("Nincs ilyen felhasználó!")
    else:
        if jelszo_ellenorzese(felhasznalo):
            print("Sikeres bejelentkezés! :)")
        else:
            print("Sikertelen bejelentkezés! :(")