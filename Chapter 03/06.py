# 6. Magic Dates
#
# The date June 10, 1960, is special because when 
# it is written in the following format, the month 
# times the day equals the year:
#
# 6/10/60
#
# Design a program that asks the user to enter a 
# month (in numeric form), a day, and a two-digit 
# year. The program should then determine whether 
# the month times the day equals the year. If so, 
# it should display a message saying the date is 
# magic. Otherwise, it should display a message 
# saying the date is not magic.

# 1. asks the user to enter a 
# month (in numeric form), a day, and a two-digit 
# year.

month = int(input('\nEnter the month from 1 thru 12: '))
day = int(input('Enter the day from 1 thru 31: '))
year = int(input('Enter the year: '))

# 65/56/56 IS 
message = '\n' + format(month) + '/' \
            + format(day) + '/' \
            + format(year) + \
            ' IS '

if ((month * day) != year):
    message += "NOT "
    
message += "magic."

# Or this could work too
# if ((month * day) == year):
#     message += 'magic.'
# else:
#     message += 'NOT magic.'

print(message, "\n\n")