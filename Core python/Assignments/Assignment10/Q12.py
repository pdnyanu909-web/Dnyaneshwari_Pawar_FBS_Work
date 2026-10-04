# Write a program to create three lists of numbers, their squares and cubes
a = [1, 2, 3, 4, 5]

square = []
cube = []

for i in a:
    square = square + [i ** 2]
    cube = cube + [i ** 3]

print("Numbers:", a)
print("Squares:", square)
print("Cubes:", cube)
