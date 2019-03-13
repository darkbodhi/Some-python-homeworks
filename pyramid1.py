total = int(input("Please, insert the number of rows: "))
y = int(1)
my_list = []
my_list.append(y)
for i in range(0, total):
    for j in range(1):
        print(*my_list)
        y += 1
        my_list.append(y)
