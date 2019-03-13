power = int(input("Please input the required power: "))
x = 1
if not power > 0:
    raise Exception("The power should be a positive natural number.")
else:
    while x <= power:
        print(2**x, end =" ")
        x += 1