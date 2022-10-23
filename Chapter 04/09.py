YEARS = 25
MILS_PER_YEAR = 1.6

output = "Years\tAmount Risen in Mils\n" \
         "----------------------- \n"

amount_risen = 0

for year in range(YEARS):
    amount_risen = (year + 1) * MILS_PER_YEAR # += MILS_PER_YEAR
    output += format(year + 1) + "\t" + format(amount_risen, '.2f') + "\n"

output += "----------------------- \n"

print(output)