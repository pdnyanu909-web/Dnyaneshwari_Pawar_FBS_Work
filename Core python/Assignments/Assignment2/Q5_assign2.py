#WAP to calculate selling price of book based on  cost price and discount.
cp = float(input('enter cost price:'))
discount = float(input('enter discount percentage:'))
discount_amount = (cp * discount) / 100
sp = cp - discount_amount
print('selling price =',sp)