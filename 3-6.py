import math


n = 6

if n%2 == 0:
    k = math.ceil(n/2)
    l = math.floor(n/2)
    for i in range(1,k+1):
        for j in range(1,(k+1)-i):
            print("A", end = "")
        for j in range(0, 2*i-1):
            if j == 0 or j==2*i-2:
                print("+", end = "")
            else:
                print("E", end = "")
        for j in range(k-i):
            print("B", end = "")
        print("")

    for i in range(0, n-1):
        for j in range(0,n-1):
            if j == i or j == n-2-i:
                print("+", end = "")
            elif j > i and j < n-2-i:
                print("E", end = "")
            elif j < i:
                print("C", end = "")
            else:
                print("D", end = "")
        if i == l-1:
            break
        print("")
else:
    k = math.ceil(n/2)
    l = math.floor(n/2)
    for i in range(1,k+1):
        for j in range(1,(k+1)-i):
            print("A", end = "")
        for j in range(0, 2*i-1):
            if j == 0 or j==2*i-2:
                print("+", end = "")
            else:
                print("E", end = "")
        for j in range(k-i):
            print("B", end = "")
        print("")

    for i in range(0, n):
        if i == 0:
            continue
        for j in range(0,n):
            if j == i or j == n-1-i:
                print("+", end = "")
            elif j > i and j < n-1-i:
                print("E", end = "")
            elif j < i:
                print("C", end = "")
            else:
                print("D", end = "")
        if i == l:
            break
        print("")