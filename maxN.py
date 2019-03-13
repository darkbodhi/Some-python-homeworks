x = int(input("Insert the number of items in the list: "))
z = 0
members = list()
while z < x:
    members.append(input("Insert the member of the list: "))
    z = z + 1
print(max(members))