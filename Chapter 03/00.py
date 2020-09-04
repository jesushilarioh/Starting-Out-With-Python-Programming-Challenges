# 3. Quarter of the Year
# Write a program that asks the user for a month as 
# a number between 1 and 12. The program should display 
# a message indicating whether the month is in the 
# first quarter, the second quarter, the third 
# quarter, or the fourth quarter of the year. 
# Following are the guidelines:
#
# • If the user enters either 1, 2, or 3, the month is in the first quarter.
# • If the user enters a number between 4 and 6, the month is in the second quarter.
# • If the number is either 7, 8, or 9, the month is in the third quarter.
# • If the month is between 10 and 12, the month is in the fourth quarter.
# • If the number is not between 1 and 12, the program should display an error.

user_month = int(input('Enter a month between 1 and 12: '))
message = ""

if user_month < 1 or user_month > 12:
    message = "Error. Month must be between 1 and 12.\n" + \
              "Rerun program and try again."
else:
    if user_month >= 1 and user_month <= 3:
        message = 'Month' + user_month + 'is in the first quarter.'

    elif user_month >= 4 and user_month <= 6:
        message = 'Month' + user_month + 'is in the second quarter.'

    elif user_month >= 7 and user_month <= 9:
        message = 'Month' + user_month + 'is in the third quarter.'
        
    elif user_month >= 10 and user_month <= 12:
        message = 'Month' + user_month + 'is in the fourth quarter.'
    