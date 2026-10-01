# Write a program to find sum of digits of a number.
def sum_digits(num):
    sum = 0
    while  num > 0:
        digits = num  % 10
        sum = sum + digits
        num = num // 10
    return sum
num = int(input('enter n:'))    
result = sum_digits(num)
print('sum of digits',result)

