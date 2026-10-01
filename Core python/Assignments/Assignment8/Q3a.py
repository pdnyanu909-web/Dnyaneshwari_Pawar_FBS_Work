#Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
def sum_of_series(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
n = int(input('enter number of terms:'))
result= sum_of_series(n)
print('sum =',result)

