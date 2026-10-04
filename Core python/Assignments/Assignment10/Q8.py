# Write a program to create a duplicate of an existing list. It should not point to same list. he pn sang clearly

a = [10, 20, 30, 40]
b = []

for i in a:
    b = b + [i]

print(b)

