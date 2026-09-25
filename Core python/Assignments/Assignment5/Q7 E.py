# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x =int(input('enter x:'))
n = int(input('enter num of terms:'))
sum = 0
den = 1
for i in range(1,n+ 1):
    sum = sum +(x ** i)/den
    den = den + 2
print('sum =',sum)    
