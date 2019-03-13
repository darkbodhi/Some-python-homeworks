x = int(input("Insert the first number: "))
y = int(input("Insert the second number: "))
if x > y and y > 0 :
    print("alpha")
elif x < 0 and y == 0 :
    print("bravo")
elif x == 0 or y == 0 :
    print("charlie")
else :
    print("zulu")