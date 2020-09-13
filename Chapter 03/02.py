# 2. Areas of Rectangles
# The area of a rectangle is the rectangle’s length 
# times its width. Write a program that asks for the 
# length and width of two rectangles. The program 
# should tell the user which rectangle has the 
# greater area, or if the areas are the same.

length_1 = float(input('Enter length for triangle #1: '))
width_1 = float(input('Enter width for triangle #1: '))

area_1 = length_1 * width_1

length_2 = float(input('Enter length for triangle #2: '))
width_2 = float(input('Enter width for triangle #2: '))

area_2 = length_2 * width_2

if area_1 > area_2:
    print('Rectangle #1 has the greatest area at', area_1, 'inches.')
elif area_2 > area_1:
    print('Rectangle #2 has the greatest area at', area_2, 'inches.')
elif area_1 == area_2:
    print('Rectangles #1 and #2 have the SAME area at', area_1, 'inches')

# YouTube Video: https://youtu.be/blNTUXl9EDs