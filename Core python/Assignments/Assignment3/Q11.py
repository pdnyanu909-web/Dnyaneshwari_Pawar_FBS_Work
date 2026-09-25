#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:


# children below 12= 30%discount
#senior citizen above 59 = 50% discount
# other = pay full

amount = float(input('enter ticket amount:'))
total = 0
for i in range(1,6):
    age = int(input('enter age of person:'))
    if age <12:
        ticket = amount -(amount*30/100)
    elif age >59:
        ticket = amount -(amount*50/100)   
    else:
        ticket = amount
        total = total + ticket 
print('total amount = ', total)
