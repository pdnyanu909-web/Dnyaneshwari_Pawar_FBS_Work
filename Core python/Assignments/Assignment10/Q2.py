# Write a program to find maximum and minimum element in a list.
list  =[ 10,20,30,68,90,9]
max = list[0]
mini = list[0]
for ind in range(len(list)):
    if list[ind] > max:
        max = list[ind]
    if list[ind] < mini:
        mini = list[ind]
print("Maximum element in the list is:", max)
print("Minimum element in the list is:", mini)

