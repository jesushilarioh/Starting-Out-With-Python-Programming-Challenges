# 9. Roulette Wheel Colors
#
# On a roulette wheel, the pockets are numbered 
# from 0 to 36. The colors of the pockets are
# as follows:
#
# • Pocket 0 is green.
# • For pockets 1 through 10, the odd-numbered 
#   pockets are red and the even-numbered pockets are black.
# • For pockets 11 through 18, the odd-numbered pockets 
#   are black and the even-numbered pockets are red.
# • For pockets 19 through 28, the odd-numbered pockets 
#   are red and the even-numbered pockets are black.
# • For pockets 29 through 36, the odd-numbered pockets 
#   are black and the even-numbered pockets are red.
#
# Write a program that asks the user to enter a pocket number 
# and displays whether the pocket is green, red, or black. 
# The program should display an error message if the user 
# enters a number that is outside the range of 0 through 36.

user_pocket_number = int(input("Enter a pocket number: "))

if user_pocket_number >= 0 and user_pocket_number <= 36:
    
    if user_pocket_number == 0:
        user_pocket_color = "green"
    
    elif user_pocket_number >= 1 and user_pocket_number <= 10:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "black"
        else:
            user_pocket_color = "red"

    elif user_pocket_number >= 11 and user_pocket_number <= 18:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "red"
        else:
            user_pocket_color = "black"
    
    elif user_pocket_number >= 19 and user_pocket_number <= 28:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "black"
        else:
            user_pocket_color = "red"

    elif user_pocket_number >= 29 and user_pocket_number <= 36:
        if user_pocket_number % 2 == 0:
            user_pocket_color = "red"
        else:
            user_pocket_color = "black"

    print("User pocket color = ", user_pocket_color)
else:
    print("Error. Number must be between 0 and 36.\nRerun program and try again.")