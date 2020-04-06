"""
PANDA PYTHON 3
"""

# Część pierwsza

# print("Hello world!")

# odpowiedz = input("podaj imie: \n")
# wiek = input("podaj swój wiek: \n")
# 
# print("Witaj " + odpowiedz + "\n" + wiek)
# 
# odpowiedzopandach = input("ile mamy pand żyjących na świecie?")
# 
# print(odpowiedzopandach)
# 
# 
# przywitanie = "Witajcie na wielki spotkaniu! %s \n masz %s \n zaś pand na świecie jest %s"
# 
# 
# print(przywitanie % (odpowiedz, wiek, odpowiedzopandach))

#
#liczba = 12
#liczba2 = "12"
#liczba3 = 2.8
#
#
#liczba10, liczba11 = 10, 11
#
#
#print(liczba10)
#print(liczba11)
#
#print("%s %s %s" % (str(liczba), str(liczba2), str(liczba3)))
# 
# print(4*int(str(4)))
# 
# print(5 ** 12)
# 
# 


dane = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent at neque ac lectus bibendum convallis. Ut nec blandit quam. Morbi efficitur lectus eros, non suscipit felis auctor ac. Pellentesque sed velit sed ligula cursus molestie. Vivamus at facilisis ex. Pellentesque eget sodales odio, sed molestie arcu. Morbi semper ac odio ut pellentesque. Maecenas massa justo, molestie sed nulla sit amet, auctor rutrum neque. Cras euismod aliquam elit a fringilla. Cras molestie turpis eget nunc fermentum congue. 
    Aenean eu diam eu magna tempor congue. ERROR: Praesent arcu sapien,<end> fermentum in orci id, iaculis vulputate ligula."""


# https://www.lipsum.com/feed/html

# print(dane)
# 
# print(dane.find("panda")) # return -1
# 
# print("diam" in dane) # True / False
# 

blad = dane.find("ERROR")
term = dane.find("<end>")

komunikat = dane[blad:term]

print(komunikat)



dane = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent at neque ac lectus bibendum convallis. Ut nec blandit quam. Morbi efficitur lectus eros, non suscipit felis auctor ac. Pellentesque sed velit sed ligula cursus molestie. Vivamus at facilisis ex. Pellentesque eget sodales odio, sed molestie arcu. Morbi semper ac odio ut pellentesque. Maecenas massa justo, molestie sed nulla sit amet, auctor rutrum neque. Cras euismod aliquam elit a fringilla. Cras molestie turpis eget nunc fermentum congue. 
    Aenean eu diam eu magna tempor congue. ERROR: Praesent arcu sapien,<end> fermentum in orci id, iaculis vulputate ligula."""



# ==
# <
# >
# >= <=
# !

a = 2

# print(dane.find("panda"))


if "panda" in dane:
    if ( a == 4):
        print(str(a) + " jest równe 4")

    else:
        print(str(a) + " nie jest równe 4")
    
    print("jest Panda")

else: 
    print("nie ma pandy")


if "ERROR1" in dane:
    a = dane.find("ERROR1")
    print(dane[a:])
elif (a==a):
    print("pierwsze True")

elif "ERROR" in dane:
    a = dane.find("ERROR")
    print(dane[a:])



else:
    print("OK")




# podaj 3 boki trójkąta
# sprawdź dane
# oblicz pole

#
#
#a,b,c =5,6,7

# str(WARTOŚĆ)
# int(WARTOŚĆ)
# float(WARTOŚĆ)


a = float(input("podaj a: "))
b = float(input("podaj b: "))
c = float(input("podaj c: "))


if (a>0 and b>0 and c>0):
    s= (a+b+c)/2
    pole = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(pole)


