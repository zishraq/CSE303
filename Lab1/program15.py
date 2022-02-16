list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

result = 0

for i in range(0, len(list1), 2):
    new_list.append(list1[i])

for i in range(1, len(list2), 2):
    new_list.append(list2[i])

print(new_list)
