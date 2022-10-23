NUMBER_OF_MONTHS = 12

numberOfYears = int(input("\nEnter number of years: "))

while numberOfYears < 0:
    numberOfYears = int(input("Error: Enter a positive number: "))

inchesOfRainfall = 0.0
totalMonths = 0
totalInchesInRainFall = 0

for year in range(numberOfYears):
    for month in range(NUMBER_OF_MONTHS):
        
        inchesOfRainfall = float(input("How how many inches of rainfall for month #" \
                                        + format(month + 1) + " in year " + "#"     \
                                        + format(year + 1) + ": "))
        
        while inchesOfRainfall < 0:
            inchesOfRainfall = float(input("Error: Enter a positive number: "))

        totalMonths += 1
        totalInchesInRainFall += inchesOfRainfall

averageRainfall = totalInchesInRainFall / totalMonths

output = "\nNumber of months         = " + format(totalMonths) + "\n"          \
         "Total inches of rainfall   = " + format(totalInchesInRainFall) + "\n" \
         "Average rainfall per month = " + format(averageRainfall) + "\n"

print(output)

