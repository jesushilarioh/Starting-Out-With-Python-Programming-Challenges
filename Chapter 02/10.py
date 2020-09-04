#1. Input
number_of_cookies = int(input('\nHow many cookies would you like to make: '))

#2. Process
COOKIES = 48
SUGAR = 1.5
BUTTER = 1
FLOUR = 2.75

total_sugar  = (SUGAR * number_of_cookies) / COOKIES
total_butter = (BUTTER * number_of_cookies) / COOKIES
total_flour  = (FLOUR * number_of_cookies) / COOKIES

#3. Output
print('\nNumber of cookies =', number_of_cookies, end='\n\n')
print('Total sugar =', format(total_sugar, ',.2f'))
print('Total butter =', format(total_butter, ',.2f'))
print('Total flour =', format(total_flour, ',.2f'), end='\n\n')