user_number = int(input("Enter a positive number: "))

while user_number < 0:
    user_number = int(input("Error: Enter a positive number: "))

total = 0

if user_number > 0:
    total = 1

    for number in range(user_number):
        total *= (number + 1)
    
output = format(total)

print(output)