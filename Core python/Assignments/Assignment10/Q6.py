# Write a program to remove duplicates from the list.
a = [ 10,20,10,30,20,40]
new = []
for i in a:
    found = False
    for j in new:
        if i == j:
            found = True
            break
    if found == False:
            new = new +[i]
print(new)       

