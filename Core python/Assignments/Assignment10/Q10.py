# Write a program to remove all occurrences of a given element in the list.
a = [10, 20, 10, 30, 10, 40]

x = int(input("Enter element to remove: "))

new = []

for i in a:
    if i != x:
        new = new + [i]

print(new)

