# Write a program to reverse the list.

a = [ 10,20,30,89,30,20]
rev = []
n = 0
i = len(a) - 1
while i >= 0:
    rev = rev + [a[i]]
    i = i - 1
print(rev)    

