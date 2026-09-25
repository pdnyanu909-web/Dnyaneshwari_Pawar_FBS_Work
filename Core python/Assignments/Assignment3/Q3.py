#WAP to input angles of a triangle and check whether triangle is valid or not

a = int(input('enter first angle:'))
b = int(input('enter second angle:'))
c = int(input('enter third angle:'))
if a+b+c == 180:
    print('triangle is valid')
else:
    print('triangle is not valid')