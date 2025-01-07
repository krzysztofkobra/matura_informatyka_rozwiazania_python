# 4.1

pierwsze = []
calkowite = []
liczba_dzielnikow = 0

with open('pliki/liczby.txt', 'r') as file:
    pierwsze = [int(x) for x in file.readline().strip().split()]
    calkowite = [int(x) for x in file.readline().strip().split()]

for p in pierwsze:
    if any(c % p == 0 for c in calkowite):
        liczba_dzielnikow += 1

print(liczba_dzielnikow)

# 4.2

pierwsze_posortowane = sorted(pierwsze, reverse=True)

print(pierwsze_posortowane[101])

# 4.3

def rozklad(n):
    czynniki = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            czynniki.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        czynniki.append(n)

    return czynniki

for c in calkowite:
    czynniki = rozklad(c)
    pierwsze_kopia = pierwsze.copy()
    mozliwe = True

    for czynnik in czynniki:
        if czynnik not in pierwsze_kopia:
            mozliwe = False
            break
        else:
            pierwsze_kopia.remove(czynnik)

    if mozliwe:
        print(c)