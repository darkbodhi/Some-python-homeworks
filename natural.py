x = int(input("Insert the number: "))
z = int(1)
if x == 0 :
        print("Input is zero. No natural row is available.")
if x > 0 :
    while x > z:
        print(z)
        z = z + 1
else :
    print("Invalid data.")