# Write a program to check whether a number is prime or not using recursion.
def prime(n,i):
    if n < 2:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n,i + 1) 
n = int(input('enter number:'))
if prime(n,2):
    print('prime number')
else:
    print('not prime number')
