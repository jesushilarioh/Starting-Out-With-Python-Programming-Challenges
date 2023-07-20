DAYS = 7
REQUIRED_SLEEP_AMOUNT = DAYS * 8

hours_slept = 0.0
total_sleep_hours = 0.0

for day in range(DAYS):
    hours_slept = float(input("How many sleep hours on day " + format(day + 1) + "? "))

    while hours_slept < 0:
        hours_slept = float(input("Error: Enter a positive number: "))

    total_sleep_hours += hours_slept

sleep_debt = REQUIRED_SLEEP_AMOUNT - total_sleep_hours

output = "\nTotal sleep debt = " + format(sleep_debt, '.2f') + "\n"

if sleep_debt > 0:
    output += "\nYou need more sleep!!\n"
else:
    output += "\nYou are sleeping well!!\n"

print(output)