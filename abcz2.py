x = int(input("Insert the first number: "))
y = int(input("Insert the second number: "))
z = int(input("Insert the third number: "))
if x + y > z :
    print("alpha")
elif y - z > x :
    print("bravo")
elif y % z == 0 :
    print("charlie")
else :
    print('zulu')