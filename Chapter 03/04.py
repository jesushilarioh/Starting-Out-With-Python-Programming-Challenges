# 4. Roman Numerals
# Write a program that prompts the user to enter 
# a number within the range of 1 through 10. 
# The program should display the Roman numeral 
# version of that number. If the number is outside 
# the range of 1 through 10, the program should 
# display an error message. The following table 
# shows the Roman numerals for the numbers 
# 1 through 10:
#
# Number      Roman Numeral
# 1           I 
# 2           II 
# 3           III 
# 4           IV 
# 5           V 
# 6           VI 
# 7           VII 
# 8           VIII 
# 9           IX
# 10          X

user_number = int(input('Enter a number between 1 and 10: '))

message = ""

if user_number < 1 or user_number > 10:
    message = "\nError. Number must be between 1 and 10." + \
              "\nRe-run program and try again."
else:
    #valid 
    message = '\nThe roman numeral for '

    if user_number == 1:
        message += format(user_number) + ' is I'
    elif user_number == 2:
        message += format(user_number) + ' is II'
    elif user_number == 3:
        message += format(user_number) + ' is III'
    elif user_number == 4:
        message += format(user_number) + ' is IV'
    elif user_number == 5:
        message += format(user_number) + ' is V'
    elif user_number == 6:
        message += format(user_number) + ' is VI'
    elif user_number == 7:
        message += format(user_number) + ' is VII'
    elif user_number == 8:
        message += format(user_number) + ' is VIII'
    elif user_number == 9:
        message += format(user_number) + ' is IX'
    elif user_number == 10:
        message += format(user_number) + ' is X'

print(message, '\n')