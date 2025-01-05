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



print(oblicz_nieparzysty_skrot(2254233292))
print(2254233292 // 10)