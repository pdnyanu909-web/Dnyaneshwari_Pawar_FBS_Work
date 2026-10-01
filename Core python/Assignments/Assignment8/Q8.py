# Write a program find reverse of a number
def reverse_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev    
num = int(input('enter n:'))    
result = reverse_num(num)
print('revers num =',result)

