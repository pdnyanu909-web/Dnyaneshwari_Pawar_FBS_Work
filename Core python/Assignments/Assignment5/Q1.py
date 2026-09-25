1.# Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_id = 'admin'
correct_password = '234'

for i in range(3):
    userid = input('enter user id:')
    password = input('enter password:')
    if userid == correct_id and password == correct_password:
        print('login successful')
        break
    else:  
        print('incorrect user id or password')
else:
    print('3 attempts completed.program terminated')