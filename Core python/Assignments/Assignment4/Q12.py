# check given number is armstrong number or not

n = int(input('enter a num:'))
temp = n
sum = 0
digits = len(str(n))
while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10
if sum == temp:
    print('armstrong num:')    
else:
    print(' not armstrong num')