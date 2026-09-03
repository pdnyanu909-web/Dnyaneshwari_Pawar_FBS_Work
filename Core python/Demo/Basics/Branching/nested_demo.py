gender = (input('enter gender:'))
age = int(input('enter age:'))
if gender == 'f':
    if age>19:
        print('female eligible for marri:')
    else:
        print('not eligible for marri') 
else:               
    if age > 21:
        print('eligible')
    else:
        print('not eligible')