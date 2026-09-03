# find roots of quadratic equation
import math
#take input
a = float(input('enter value of a:'))
b = float(input('enter value of b:'))
c = float(input('enter value c:'))

# calculae  formula
d = b**b - 4*a*c
#calculate roots
Root1 = (-b+ math.sqrt(d))/(2*a)
Root2 = (-b - math.sqrt(d))/(2*a)
#display result
print('root 1:',Root1)
print('root 2:',Root2)