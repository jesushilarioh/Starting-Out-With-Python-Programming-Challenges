starting_number_of_organisims = int(input("\nStarting number of organisims: "))

while starting_number_of_organisims < 0:
    starting_number_of_organisims = int(input("Error: Enter a positive number: "))

average_daily_increase = float(input("Average daily increase: "))

while average_daily_increase < 0:
    average_daily_increase = float(input("Error: Enter a positive number: "))

average_daily_increase /= 100

number_of_days_to_multipy = int(input("Number of days to multiply: "))

while number_of_days_to_multipy < 0:
    number_of_days_to_multipy = int(input("Error: Enter a positive number: "))

output = "\nDay Approx.\tPopulation\n" + \
         "----------------------------------\n"

population = starting_number_of_organisims

for day in range(number_of_days_to_multipy):

    if day == 0:
        output += format(day + 1) + "\t\t" + format(population) + "\n"
    
    else: 
        population += (population * average_daily_increase)
        output += format(day + 1) + "\t\t" + format(population) + "\n"

output += "----------------------------------\n"

print(output)