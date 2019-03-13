y = int(input("Please insert the number which will be factorizing: "))
power = int(input("Please input the required power: "))
x = 0
if not power > 0:
    raise Exception("The power should be a positive natural number.")
while x <= power:
    print(y**x, end = " ")
    x += 1