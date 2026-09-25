length = float(input('enter length  of wall:'))
height = float(input('enterheight of wall:'))
rate = float(input('enterpainting rate per sq.m:'))
if length > 0 and height > 0 and rate > 0:
    area = 4 * length * height
    cost = area * rate 
    print('total painting cost=',cost)
else:
    print('invalid input')