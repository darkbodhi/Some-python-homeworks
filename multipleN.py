x = int(input("Insert the number which will be divided: "))
y = int(input("Insert the number on which the first number will be divided: "))
z = int(0)
if x <= 0 or y == 0 or x % y != 0:
    print("Invalid data.")
else :
    while z < x :
        print(z)
        z = z + y