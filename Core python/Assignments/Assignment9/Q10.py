# Write a program to reverse a number using recursion.

def reverse(n, rev = 0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse(n // 10,rev)
num = int(input('enter num:'))        
result = reverse(num)
print('reverse num:',result)


