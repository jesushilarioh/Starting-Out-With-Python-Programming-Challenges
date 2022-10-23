
KILOMETERS = 1.60934

output = "\nMiles\t\tKilometers\n" \
         "-----------------------\n"

for mile in range(10, 81, 10):
    output += format(mile) + "\t\t" + format((mile * KILOMETERS), '.2f') + '\n'

output += '\n'

print(output)