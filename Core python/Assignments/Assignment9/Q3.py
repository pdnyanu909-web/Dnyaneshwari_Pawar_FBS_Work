# Write a program to reverse a given number using recursive function.

def reverse(n,rev = 0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse( n // 10,rev)
num = int(input('enter a num:'))        
result = reverse(num)
print('reverse num: ',result)             

