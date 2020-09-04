#1. Input
R = float(input('Enter the length of the row, in feet: '))
E = float(input('Enter amount of space used by an end-post assembly: '))
S = float(input('Enter amount of space between vines: '))

#2. Process
V = (R - (2 * E)) / S

#3. Output
print('Number of grapevines that will fit in a row = ', V)