#Input 5 subject marks from user and display grade(eg.First class,second class)

m1 = int(input('enter subject1:'))
m2 = int(input('enter subject2:'))
m3 = int(input('enter subject3:'))
m4 = int(input('enter subject4:'))
m5 = int(input('enter subject5:'))

total = m1+m2+m3+m4+5
percentage = total/5
print('total',total)
print('percentage',percentage)

if percentage >= 90:
    print('First class')
elif percentage > 75:
    print('second class')
elif percentage > 60:
    print('third class')
elif percentage > 50:
    print('fourth class')
elif percentage > 35:
    print('fifth class')
else:
    print('fail')