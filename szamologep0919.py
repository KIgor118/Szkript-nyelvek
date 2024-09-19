print("Számológép")

jel = input("Müveleti jel (+,-,*,/): ")

if jel == "+" or jel == "-" or jel == "*" or jel == "/":
    elso = input("Egyik szám: ")
    masodik = input("Másik szám: ")
else:
    exit()

if jel == "+":
    osszeg = int(elso)+int(masodik)
    print(elso,"+",masodik,"=",osszeg)
elif jel == "-":
    osszeg = int(elso)-int(masodik)
    print(elso,"-",masodik,"=",osszeg)
elif jel == "*":
    osszeg = int(elso)*int(masodik)
    print(elso,"*",masodik,"=",osszeg)
elif jel == "/":
    osszeg = int(elso)/int(masodik)
    print(elso,"/",masodik,"=",osszeg)
else:
    print("valami nem jó")


