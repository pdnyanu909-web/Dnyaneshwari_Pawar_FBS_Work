# Write a program to print Fibonacci series using recursion.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1)  +fibonacci (n - 2)
num = int(input('enter num of terms:'))        
for i in range(num):
    print(fibonacci(i),end = ' ')