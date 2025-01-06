# 3.1

def oblicz_nieparzysty_skrot(n):
     skrot = 0
     mnoznik = 1

     while n > 0:
         cyfra = n % 10
         if cyfra % 2 == 1:
             skrot = skrot + cyfra * mnoznik
             mnoznik *= 10
         n //= 10
     return skrot

print(oblicz_nieparzysty_skrot(294762))
print(oblicz_nieparzysty_skrot(39101))
print(oblicz_nieparzysty_skrot(224))

# 3.2

liczby = []
najwieksza = 0
ile_nie_ma = 0

plik = open('pliki/skrot.txt', 'r')
for linia in plik:
    liczba = int(linia.strip())
    liczby.append(liczba)

for liczba in liczby:
    if oblicz_nieparzysty_skrot(liczba) == 0:
        ile_nie_ma = ile_nie_ma + 1
        if liczba > najwieksza:
            najwieksza = liczba

print(f"ile liczb nie ma skrotu: {ile_nie_ma}, najwieksza z nich: {najwieksza}")

# 3.3 pewnie dałoby się ładniej i może krócej ale działa

import math

liczby2 = []
skroty = []

plik2 = open('pliki/skrot2.txt', 'r')
for linia in plik2:
    liczba = int(linia.strip())
    liczby2.append(liczba)
    skroty.append(oblicz_nieparzysty_skrot(liczba))

for i in range(len(liczby2)):
    if math.gcd(liczby2[i], skroty[i]) == 7:
        print(liczby2[i])