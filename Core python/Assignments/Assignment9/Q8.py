# Write a program to check if given number is Armstrong or not using recursive function.

def power(a,b):
    if b == 0:
        return 1
    return a * power(a,b-1)


def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)


def armstrong(n,digits):
    if n == 0:
        return 0
    digit = n % 10
    return power(digit,digits) + armstrong(n // 10,digits)

num = int(input('enter n :'))
digits = count_digits(num)
sum = armstrong(num,digits)

if sum == num:
    print('armstrong number')
else:
    print('not armstrong number')
    
