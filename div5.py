minimum = int(input("Please insert the minimal number: "))
maximum = int(input("Please insert the maximal number: "))
x = minimum % 5
if not maximum > minimum:
    raise Exception("Error: the relation between numbers is not minimum-maximum.")
elif x > 0:
    minimum += 5 - x
    while minimum <= maximum:
        print(minimum)
        minimum += 5
elif x == 0:
    while minimum <= maximum:
        print(minimum)
        minimum += 5
else:
    raise Exception("An error has occurred.")