minimum = int(input("Please insert the minimal number: "))
maximum = int(input("Please insert the maximal number: "))
if not maximum > minimum:
    raise Exception("Error: the relation between numbers is not minimum-maximum.")
elif minimum % 3 == 1:
    minimum += 2
    while minimum <= maximum:
        print(minimum)
        minimum += 3
elif minimum % 3 == 2:
    minimum += 1
    while minimum <= maximum:
        print(minimum)
        minimum += 3
elif minimum % 3 == 0:
    while minimum <= maximum:
        print(minimum)
        minimum += 3
else:
    raise Exception("An error has occurred!")