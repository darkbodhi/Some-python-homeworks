x = int(input("Insert the size of the numeric square: "))
y = 1
length = list()
depth = int(1)
while y <= x:
    length.append(y)
    y += 1
while depth <= x:
    print(*length, sep =" ")
    depth += 1