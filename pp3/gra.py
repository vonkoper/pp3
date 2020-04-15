from random import seed
from random import randint
from datetime import date

seed(1)
# energia = 10 
# droga = 0
wyniki = []
gra = True


def wydarzenie_1(droga, energia):
    print("Panda idzie dalej")
    droga = droga + 1 
    energia = energia -1
    return droga, energia

def wydarzenie_2(droga, energia):
    print("Panda się zgubiła")
    energia = energia - 2
    return droga, energia

def wydarzenie_3(droga, energia):
    print("Panda sie zdrzemnela")
    energia = energia + 2
    return droga, energia


print("#########START")
while gra:
    energia = 10 
    droga = 0
    while energia > 0 and droga < 8: 
        print("stan pandy: " + str(energia) + " : " + str(droga))
        wydarzenie = randint(1,4)
        print("wydarzenie " + str(wydarzenie))

        if wydarzenie == 1:
            droga, energia = wydarzenie_1(droga, energia)
        elif wydarzenie == 2: 
            droga, energia = wydarzenie_2(droga, energia)
        elif wydarzenie == 3: 
            droga, energia = wydarzenie_3(droga, energia)

        if droga >= 8:
            print("Panda dotarła do celu -- Wynik: " + str(droga))
            dodanie_wyniku = input("Dodac wynik? TAK/NIE >")
            if dodanie_wyniku == "TAK":
                teraz = date.today()
                wyniki.append(str(teraz) + " Zwycieztwo")
                print(wyniki)
            gramy_dalej = input("Grasz dalej? TAK/NIE")
        elif energia <= 0:
            print("Panda nie dotarła do celu")
        
    
    if gramy_dalej == "NIE":
        gra = False
    