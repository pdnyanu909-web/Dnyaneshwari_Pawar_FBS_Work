num = 567
d1 = num % 10  #7
num = num // 10 #56
print(d1)

d2 = num % 10 #6
num = num // 10 #5
print(d2)

d3 = num % 10 #5
num = num // 10 #0
# print(d3)
print(f'd1:{d1}, d2:{d2}, d3:{d3}')
