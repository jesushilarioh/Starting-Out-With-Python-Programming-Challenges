# 1. Bug Collector 
# A bug collector collects bugs everyday for five days. Write a program that keeps a running total of the number of bugs collected during the five days. The loop should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected.

NUMBER_0F_DAYS = 5
dailyCollection = 0
total5DayCollection = 0
message = ''

for day in range(NUMBER_0F_DAYS):

    dailyCollection = int(input("How many bugs collected on day " + format(day + 1) + ': '))

    while dailyCollection < 0:
        dailyCollection = int(input("Error. Enter a positive number: "))

    total5DayCollection += dailyCollection

message = 'Total number of bugs collected for 5 days = ' + format(total5DayCollection);

print(message)