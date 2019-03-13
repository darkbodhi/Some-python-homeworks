minimum = int(input("Please insert the minimal number: "))
maximum = int(input("Please insert the maximal number: "))
divisor = int(input("Please insert the number on which the first one will be divided: "))
x = minimum % divisor
if divisor <= 0:
    raise Exception("An error has occurred. The divisor is not a natural positive number.")
elif not maximum > minimum:
    raise Exception("Error: the relation between numbers is not minimum-maximum.")
elif x == 0:
    while minimum <= maximum:
        print(minimum)
        minimum += divisor
elif x > 0:
    minimum += divisor - x
    while minimum <= maximum:
        print(minimum)
        minimum += divisor
else:
    raise Exception("An error has occurred.")