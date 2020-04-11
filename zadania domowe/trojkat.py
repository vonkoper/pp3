'''
Napisać program który sprawdzi czy z podanych przez użytkownika długości boków jest możliwość stworzenia trójkąta i oblicza jego pole. 

'''

a=float(input("Podaj dlugosc pierwszego boku trojkata: "))
b=float(input("Podaj dlugosc drugiego boku: "))
c=float(input("Podaj dlugosc trzeciego boku: "))

dlugosci_bokow = [a, b, c]
x=max(dlugosci_bokow)

dlugosci_bokow.remove(x)

print(dlugosci_bokow)

if sum(dlugosci_bokow) > x:

    answer=input("Z takich odcinkow da sie zbudowac trojkat, czy chcesz policzyc jego powierzchnie? (y/n) ")
    if answer == "y":
        ob=0.5*(a+b+c)
        pole=(ob*(ob-a)*(ob-b)*(ob-c))**0.5
        print("Pole trojkata wynosi: ", pole)
    if answer == "n":
        print("Koniec")
        
else:
    print("Z takich odcinkow nie da sie zbudowac trojkata.")