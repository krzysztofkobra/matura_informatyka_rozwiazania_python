# 2.1
def liczba_nieujemna(n):
    b = 1
    c = 0
    licznik = 0
    while n > 0:
        a = n % 10
        n = n // 10
        if(a % 2 == 0):
            c = c + b * (a // 2)
        else:
            c = c + b
            licznik = licznik + 1
        b = b * 10
    return (f"wartość c: {c}, liczba wykonań: {licznik}")

print(liczba_nieujemna(33658))
print(liczba_nieujemna(542102))
print(liczba_nieujemna(87654321012345678))

# 2.2

print(liczba_nieujemna(333333666666999999)) # tu interesuje nas tylko wartość c