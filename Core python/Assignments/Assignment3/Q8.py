import random

userid = input('enter userid:')
password= input('enter password:')

if userid =='dnyanu' and password == '123':
    num =random.randint(1000,9999)
    print('random num is num:',num)
    user_num = int(input('enter the same num:'))
    if user_num == num:
        print('success')
    else:
        print('failed')
else:
    print('invalid userid or password')