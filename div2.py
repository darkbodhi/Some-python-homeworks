minimum = int(input("Please insert the minimal number: "))
maximum = int(input("Please insert the maximal number: "))
if not maximum > minimum:
    raise Exception("Error: the relation between numbers is not minimum-maximum.")
elif minimum % 2 == 0:
    while minimum <= maximum:
        print(minimum)
        minimum += 2
elif minimum % 2 == 1:
    minimum += 1
    while minimum <= maximum:
        print(minimum)
        minimum += 2
else:
    raise Exception("Mistake!")