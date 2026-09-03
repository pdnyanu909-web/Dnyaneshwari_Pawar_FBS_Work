# find the sum of three digit number
num =int(input('enter three digit num:'))
a = num // 100
b = (num // 10) % 10
c = num % 10

total = a+b+c
print('sum of digits =', total)