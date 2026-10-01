# Write a program to check if entered number is a palindrome or not
def palindrome(num):
    original = num 
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10+digit
        num = num // 10
    if original == rev:
        return True
    else:
        return False
num = int(input('enter num:'))
if palindrome(num):
    print('palindrome number')
else:
    print('not a palindrome number')

