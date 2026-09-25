# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input('enter n :'))
sum = 0
term = 1
for  i in range(n):
    sum = sum + term
    term = term * 2
print('sum =',sum)    