
save = []
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        save.append("FizzBuzz")
        # print("FizzBuzz")
    if i%3 == 0 and i%5 != 0:
        save.append("Fizz")
        # print("Fizz")
    if i%3 != 0 and i%5 == 0:
        save.append("Buzz")
        # print("Buzz")
    if i%3!=0 and i%5 !=0:
        save.append(str(i))
        # print(str(i))

for i in range(0,100):
    print(save[i], end =" ")