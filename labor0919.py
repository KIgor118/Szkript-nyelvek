print("Jövedelem számítás\n")

brutto = int(input("Bruttó jövedelme: "))
kor = int(input("Kora: "))

if kor < 25:
    if brutto > 599790:
        szja = (brutto - 599790) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

nyugdij = brutto * 0.1
tb = brutto * 0.07
munkanelkuli = brutto * 0.015
netto = brutto - szja - nyugdij - tb - munkanelkuli

print("Jövedelem".center(40))
print("SZJA:".ljust(15,"."), str(int(szja)).rjust(25,".")," Ft",sep="")
print("Nyugdíj:".ljust(15,"."), str(int(nyugdij)).rjust(25,".")," Ft",sep="")
print("TB:".ljust(15,"."), str(int(tb)).rjust(25,".")," Ft",sep="")
print("Munkanélküli:".ljust(15,"."), str(int(munkanelkuli)).rjust(25,".")," Ft",sep="")
print("Nettó:".ljust(15,"."), str(int(netto)).rjust(25,".")," Ft",sep="")

