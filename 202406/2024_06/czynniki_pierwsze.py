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

print(rozklad(10))