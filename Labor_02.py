print ("Szia DUE!",end='')

print("\tSzia", "DUE!")

print("Szia","DUE!",sep="-")

print("Szia","\n\tDUE!")

print('''Szép napounk
lesz ma!
''')

felhasznalo_neve= "Józsi"
felhasznalo_kora= 21

print("Szia",felhasznalo_neve)
print(f"Szia {felhasznalo_neve}")

print("neve: {0} ,\nkora: {1}".format(felhasznalo_kora,felhasznalo_kora) )

print(felhasznalo_neve.rjust(50,"."))
print(str(felhasznalo_kora).rjust(50,"."))

print(felhasznalo_neve.ljust(50,"."))
print(str(felhasznalo_kora).ljust(50,"."))

print(felhasznalo_neve.center(50,"."))
print(str(felhasznalo_kora).center(50,"."))

felhasznalo_neve=input("\nKérem a nevét: ")
felhasznalo_kora=input("Hány éves vagy: ")

print("\nSzia",felhasznalo_neve)
print("Biztosan ",felhasznalo_kora, " éves vagy? Nem", int(felhasznalo_kora) + 10)
