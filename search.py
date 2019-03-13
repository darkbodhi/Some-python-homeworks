needle = int(input("Insert the searched for number: "))
x = int(input("Insert the number of the items in the list: "))
y = 0
q = -1
members = list()
while y < x:
    members.append(int(input("Enter the member of the list: ")))
    y += 1
    if members.count(needle) == 1:
        q = y

print(q)
