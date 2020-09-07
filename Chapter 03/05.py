# 5. Mass and Weight
# Scientists measure an object’s mass in kilograms 
# and its weight in newtons. If you know the amount 
# of mass of an object in kilograms, you can calculate 
# its weight in newtons with the following formula:
#
# weight = mass x 9.8
#
# Write a program that asks the user to enter an 
# object’s mass, then calculates its weight. If the 
# object weighs more than 500 newtons, display a 
# message indicating that it is too heavy. If the 
# object weighs less than 100 newtons, display a 
# message indicating that it is too light.

mass = float(input('Enter an object\'s mass: '))

weight = mass * 9.8

message = "\nThe object"

if weight < 100:
    message += ' is too light at ' + format(weight, ',.2f') + ' newtons.'
elif weight >= 100 and weight <= 500:
    message += '\'s weight at ' + format(weight, ',.2f') + ' is just right.'
elif weight > 500:
    message += ' is too heavy at ' + format(weight, ',.2f') + ' newtons.'

print(message, end="\n\n")