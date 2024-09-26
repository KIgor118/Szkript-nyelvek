import Labor_04_modul


adatok = Labor_04_modul.adatok_bekerese()

eredmeny = Labor_04_modul.muveletek_vegrehajtasa(adatok[0], adatok[1], adatok[2])

Labor_04_modul.eredmenyek_megjelenitese(adatok[0], adatok[1], adatok[2], eredmeny)