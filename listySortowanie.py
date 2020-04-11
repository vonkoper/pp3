lista = [1,5,62,6,9,0,1,3,6,100]

dlugosc_listy = len(lista)
print(dlugosc_listy)

a = int(dlugosc_listy/2)
lista2 = lista[a:]

print(lista2)


print(lista.sort())
lista2 = lista[5:]
lista3 = lista[:5]


print(lista)
print(lista2)
print(lista3)


lista_odwrocona = lista.sort(reverse=True)

print(lista)


lista.insert(0,0)

print(lista)
 
 
print(lista)
lista.append(lista2)
 
print(len(lista))
 
 
print(lista[10])
 
 
# Nieładny sposób wypisywania elementu tablicy w tablicy
#aa = lista[10]
#bb = aa[0]
#print(bb)
 
lista[10][0] = 3
 
print(lista[10])
 
 
lista[10][0] = [1,2,"Panda"]
 
print(lista)


# Krotki
krotka_a = ("Panda", 2, 4)
 
print(krotka_a[0])
 
krotkapandy = 1, 2, 3
 
print(krotkapandy)
 
 
panda1, panda2, panda3 = krotkapandy
 
 
print(panda1)
print(panda2)
print(panda3)

 
print("############")
 
krotka_b = (10,11,12,14)
 
panda10, panda11, *panda12 = krotka_b
 
print(panda10)
print(panda11)
print(panda12[0])

#SŁOWNIKI
pandaslownik = {}
pandaslownik1 = dict(klucz1="wartość1")
pandaslownik2 = {"klucz2": "wartość2"}

#print(pandaslownik.keys())

print(pandaslownik1.keys())
print(pandaslownik2.keys())


print(pandaslownik.values())
print(pandaslownik1.values())
print(pandaslownik2.values())
print(pandaslownik1["klucz1"])




pandaslownik["panda"] = "Jest wielka"
pandaslownik["panda"] = "Jest wielka2"

zly_slownik = {"klucz2": "wartość2", "klucz2": "wartość3"}
print(zly_slownik)
print(pandaslownik)

print("############")

lista_z_duplikatami = [1,1,2,2,3]
print(lista_z_duplikatami)
lista_bez_duplikatow = list(dict.fromkeys(lista_z_duplikatami))
print(lista_bez_duplikatow)
print("############")


print("klucz1" in zly_slownik)


dobry_slownik = {"klucz1": "wartość2", "klucz2": "wartość3", "klucz3": "wartość3"}

for each in dobry_slownik:
    print(dobry_slownik[each])


















