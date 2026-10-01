# Write a program to find sum of n numbers using recursion.
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)
num = int(input('enter num:'))    
result = sum_n(num)
print('sum =',result)

