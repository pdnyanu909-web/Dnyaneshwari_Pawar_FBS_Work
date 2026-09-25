#WAP to check if person is eligible to marry or not(male age >21 and female age >18)


gender = str(input('enter gender:'))
age = int(input('enter age:'))
if gender == 'f':
    if age >= 18:
        print('female eligible for marry')
    else:
        print('female not eligible to marry')   
else:
    if age >=21:
        print('male eligible for marry')        
    else:
        print(' male not eligible for marry')    
  