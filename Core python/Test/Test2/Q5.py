p1 = float(input('enter price 1:'))
p2 = float(input('enter price 2:'))
p3 = float(input('enter price 3:'))
p4 = float(input('enter price 4:'))
p5 = float(input('enter price 5:'))
total = p1+p2+p3+p4+p5
if total > 0:
    gst = total * 18 / 100
    bill = total + gst
    print('total bill =',bill)
else:
    print('invalid price')