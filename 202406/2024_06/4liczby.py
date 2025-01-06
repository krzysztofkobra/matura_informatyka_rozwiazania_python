# 4.1

pierwsze = []
calkowite = []
liczba_dzielnikow = 0

with open('pliki/liczby_przyklad.txt', 'r') as file:
    pierwsze = [int(x) for x in file.readline().strip().split()]
    calkowite = [int(x) for x in file.readline().strip().split()]

for p in pierwsze:
    if any(c % p == 0 for c in calkowite):
        liczba_dzielnikow += 1

print(liczba_dzielnikow)