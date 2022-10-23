pennies = 0.01

number_of_days = int(input("Enter the number of days: "))

while number_of_days < 0:
    number_of_days = int(input("Error: Enter positive number: "))

output = "\nDay\tPay\n" \
         "------------------\n"

total_pay = 0.0
day_pay = 0.0

for day in range(number_of_days):

    day_pay = pennies

    output += format(day + 1) + "\t$" + format(day_pay, '.2f') + "\n"

    total_pay += day_pay

    pennies *= 2

output += "------------------\n" \
          "Total pay = $" + format(total_pay, '.2f') + "\n"

print(output)
