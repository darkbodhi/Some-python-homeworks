x = int(input("Insert the size of the numeric square: "))
y = 1
z = int()
length = list()
depth = int(1)
while y <= x:
    length.append(y)
    y += 1
while depth <= x:
    print(*length, sep=" ")
    depth += 1
    y += -x
    z = max(length)
    length[:] = []
    while z < depth*x:
        length.append(z+1)
        z += 1