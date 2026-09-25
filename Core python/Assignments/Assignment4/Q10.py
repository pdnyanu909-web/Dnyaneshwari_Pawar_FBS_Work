# check given number is perfect number

n = int(input('enter a num :'))
sum = 0

for i in range(1,n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print('perfect num:')   
else:
    print('not perfect num')