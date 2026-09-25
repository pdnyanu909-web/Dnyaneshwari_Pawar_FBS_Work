# WAP calculate profit or loss

cp  = float(input('enter cost price:'))
sp = float(input('enter selling price:'))
if sp > cp:
    profit = sp - cp
    print('profit =',profit)
elif cp > sp:    
    loss = sp - cp
    print('loss',loss)
else:
    print('no profit no loss')
