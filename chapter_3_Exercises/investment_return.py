p = 1000
r =  7 / 100

n = 1
while n < 31:
    a = p * (1 + r)  ** n
    n += 1
    print(a)