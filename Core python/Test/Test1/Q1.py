length = float(input('enter the length :'))
breadth = float(input('enter the breath:'))
radius = float(input('enter the radius:'))

area = (length * breadth)+(3.14* radius * radius ) / 2
perimeter = (2 * length) + breadth + (2 * 3.14 * radius)
print('area=', area)
print('perimeter=', perimeter)