x = int(input("Insert the number: "))
y = int(0)
if x % 2 == 0:
    y = y + 1
    print("alpha\n")
    if x % 3 == 0:
        y = y + 1
        print("bravo\n")
    if x % 5 == 0:
        y = y +1
        print("charlie\n")
    if x % 7 == 0:
        y = y + 1
        print("zulu\n")
    print(y)
else:
    print("Invalid data. Try again.")
