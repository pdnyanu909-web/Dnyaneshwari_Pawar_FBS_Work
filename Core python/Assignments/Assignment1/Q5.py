# compound interest
# take input
P = float(input('enter principal:'))
T = float(input('enter time:'))
R = float(input('enter rate:'))
# calculate amount
Amount =  P * (1+R/100) **T
#calculate compound interest
CI = Amount - P
 # display result
print('compund interest:',CI)