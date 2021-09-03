# 8. Hot Dog Cookout Calculator
# 
# Assume hot dogs come in packages of 10, and hot dog 
# buns come in packages of 8. Write a program that 
# calculates the number of packages of hot dogs and 
# the number of packages of hot dog buns needed for a 
# cookout, with the minimum amount of leftovers. The 
# program should ask the user for the number of people 
# attending the cookout and the number of hot dogs each 
# person will be given. The program should display the 
# following details:
# 
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over
############

number_of_people = int(input("Enter number of people: "))
number_of_hotdogs_per_person = int(input("Enter number of hot dogs: "))

NUMBER_OF_HOTDOGS_PER_PACKAGE = 10
NUMBER_OF_BUNS_PER_PACKAGE = 8

total_number_of_hotdogs = number_of_people * number_of_hotdogs_per_person

number_of_hotdog_packages_needed = total_number_of_hotdogs // NUMBER_OF_HOTDOGS_PER_PACKAGE
number_of_hotdog_buns_needed = total_number_of_hotdogs // NUMBER_OF_BUNS_PER_PACKAGE
number_of_hotdogs_left_over = total_number_of_hotdogs % NUMBER_OF_HOTDOGS_PER_PACKAGE
number_of_hotdog_buns_left_over = total_number_of_hotdogs % NUMBER_OF_BUNS_PER_PACKAGE

print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", number_of_hotdog_buns_needed)
print("Number of hot dogs left over =", number_of_hotdogs_left_over)
print("Number of hot dogs buns left over =", number_of_hotdog_buns_left_over)
