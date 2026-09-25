#WAP program to check if given 3 digit number is palindrome or not

num = int(input('enter num:'))
original = num 

last = num % 10
num = num // 10

middle = num % 10
num = num // 10

first = num % 10
num = num// 10

reverse = last * 100 + middle * 10 +first
if original == reverse:
    print('palindrome')
else:
    print('not palindrome')

