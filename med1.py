
n = 20
prime = []

for i in range(2, n+1):
    if_prime = True
    for j in range(2, i):
        if i%j == 0:
            if_prime = False
    if if_prime == True:
        prime.append(i)

for i in prime:
    print(i, end = " ")