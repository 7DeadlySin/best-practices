
n = 6
for i in range(1,n+1):
    for j in range(1,(n+1)-i):
        print(" ", end = "")
    for j in range(0, i):
        print("*", end = "")
    print("")