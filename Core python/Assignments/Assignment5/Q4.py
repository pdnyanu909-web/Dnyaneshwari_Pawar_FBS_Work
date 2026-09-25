# 4. WAP to print Armstrong number within a given range 
start = int(input('enter starting number:'))
end = int(input('enter ending number:'))
for num in range(start, end+1):
    original = num
    sum = 0
    while original > 0:
        digit = original % 10
        sum = sum + digit **3
        original = original // 10
    if sum == num:
        print(num)

