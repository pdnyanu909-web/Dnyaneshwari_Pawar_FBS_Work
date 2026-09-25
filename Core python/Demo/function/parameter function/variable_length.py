# to pass multiple para to function
# mention asterisk * symbol before para
#  in funtion defination 
# value will be store in tuple format
# use for loop to iterate value from tuple
 




def addition(*num):
    sum = 0
    for val in num:
        sum += val
    return sum    
res = addition(10,20,30,40,50)    
print(res)

