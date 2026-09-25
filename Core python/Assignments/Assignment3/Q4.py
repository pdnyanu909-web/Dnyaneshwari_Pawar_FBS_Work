# WAP  to input all sides of triangle and check whether triangle is valid or not

a = int(input('enter first side:'))
b = int(input('enter second side:'))
c = int(input('enter third side:'))

if a+b>c and a+c>b and b+c>a:
    print('valid triangle')
else:    
    print('invalid triangle')