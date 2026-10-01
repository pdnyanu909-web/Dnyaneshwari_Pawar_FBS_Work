# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.
def armstrong(num):
    original = num
    sum = 0
    digits =len(str(num))
    while num > 0:
        digit = num % 10
        sum = sum + digit ** digits
        num = num // 10
    if original == sum:
        return True
    else:
        return False
num = int(input('enter num:'))        
if armstrong(num):
    print('armstrong number')
else:
    print('not an armstrong number')