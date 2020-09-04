import math
#1. Input
radius = float(input('\nEnter the radius of a circle: '))

#2. Process
area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

#3. Output
print('Radius =', radius)
print('Area =', area)
print('Circumference = ', circumference, end='\n\n')