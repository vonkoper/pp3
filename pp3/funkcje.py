zmienna_z_modulu = "test"

def potega_dla_liczb(poczatek, koniec, potega):
    koniec = koniec+1
    for liczba in range(int(poczatek), int(koniec)):
        print(str(liczba) + ": " + str(liczba**potega))

