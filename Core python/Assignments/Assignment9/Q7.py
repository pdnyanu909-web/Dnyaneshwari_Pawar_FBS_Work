# Write a program to find sum of digits using recursion.

def sum_digit(n):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return digit + sum_digit(n // 10)
num = int(input('enter num:'))        
result = sum_digit(num)
print('sum of digit =',result)


