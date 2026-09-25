num = int(input('enter 3 digit number:'))
first = num // 100
second = (num // 10)% 10
third = num % 10

if first == second * 2 and first == third / 2:
    print('yes,you have done it')
else:
    print('please try next time')