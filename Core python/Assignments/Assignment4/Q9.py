# print all numbers in a range divisible by a given number

start = int(input('enter starting num:'))
end = int(input('enter ending num:'))
n = int(input('enter divisor:'))

for i in range(start,end +1):
    if i % n == 0:
        print(i)