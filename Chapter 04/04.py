


speed = int(input("\nEnter the speed: "))
while speed < 0:
    speed = int(input("Error: Enter a positve number: "))

hours = int(input("\nEnter the hours: "))
while hours < 0:
    hours = int(input("Error: Enter a positve number: "))

distance = 0

output = "\nHour    Distance Traveled\n" \
         "-------------------------\n"

for hour in range(hours): #4 - 0, 1, 2, 3
    distance = speed * (hour + 1) # 1, 2, 3, 4

    output += format(hour + 1) + "    " + \
              format(distance) + "\n"

print(output)