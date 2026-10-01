# WAP to print first n prime numbers
n = int(input('enter n:'))
count = 0
num = 2
while count < n:
    i = 2
    flag = True
    while i < num:
        if num % i == 0:
            flag = False
            break
        i += 1
    if flag:
        print(num, end=' ')
        count += 1
    num += 1