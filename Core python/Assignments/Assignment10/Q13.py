# Write a program to print list after removing even numbers.

a = [ 2,3,4,5,6,7,8,9,10]
new = []
for i in a:
    if i % 2 != 0:
        new = new +[i]
print(new)        
