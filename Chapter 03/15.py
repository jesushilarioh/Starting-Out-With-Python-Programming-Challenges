# 15. Time Calculator
# Write a program that asks the user to enter a number of 
# seconds and works as follows:
# • There are 60 seconds in a minute. If the number of 
# seconds entered by the user is greater than or equal to 
# 60, the program should convert the number of seconds to 
# minutes and seconds.
# • There are 3,600 seconds in an hour. If the number of 
# seconds entered by the user is greater than or equal to 3,600, 
# the program should convert the number of seconds to hours, 
# minutes, and seconds.
# • There are 86,400 seconds in a day. If the number of 
# seconds entered by the user is greater than or equal to 
# 86,400, the program should convert the number of seconds to 
# days, hours, minutes, and seconds.

number_of_seconds = int(input("Enter number of seconds: "))
message = ""

if number_of_seconds < 0:
    message = "Enter a number above 0.\n" + \
              "Rerun program and try again."
else:
    if number_of_seconds >= 0 and number_of_seconds < 60:
        seconds = format(number_of_seconds % 60)
        message = "Seconds = " + seconds
    elif number_of_seconds >= 60 and number_of_seconds < 3600:
        minutes = format(number_of_seconds // 60)
        seconds = format(number_of_seconds % 60)
        message = "Minutes = " + minutes + \
                  " Seconds = " + seconds
    elif number_of_seconds >= 3600 and number_of_seconds < 86400:
        hours = format(number_of_seconds // 3600)
        minutes = format((number_of_seconds % 3600) // 60)
        seconds = format((number_of_seconds % 3600) % 60)
        message = "Hours = " + hours + " " + \
                  "Minutes = " + minutes + " " + \
                  "Seconds = " + seconds + " "
    elif  number_of_seconds >= 86400:
        days = format(number_of_seconds // 86400)
        hours = format((number_of_seconds % 86400) // 3600)
        minutes = format(((number_of_seconds % 86400) % 3600) // 60)
        seconds = format(((number_of_seconds % 86400) % 3600) % 60)
        message = "Days = " + days + " " + \
                  "Hours = " + hours + " " + \
                  "Minutes = " + minutes + " " + \
                  "Seconds = " + seconds + " "

print(message)