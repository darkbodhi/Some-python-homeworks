x = int(input("Insert the size of the numeric square: "))
y = int(x*x)
for i in range(0, x):
    for j in range(0, x):
        print((y - x) + 1, end=" ")
        y += 1
        if (y) % x == 0:
            print(" ")
            y = y - 2*x