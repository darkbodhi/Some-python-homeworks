total = int(input("Please, insert the number of rows: "))
y = int(1)
counter = int(0)
my_list = []
my_list.append(y)
for counter, i in enumerate(range(0, total)):
    for j in range(1):
        print(*my_list, end=" ")
        my_list.clear()
        for w in range(counter):
            y += 1
            my_list.append(y)