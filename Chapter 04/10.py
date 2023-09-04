

TUITION_INCREASE = .03
YEARS = 5

variable_tuition = 8000.00
output = "\nYear\tIncrease\tTuition Cost\n" + \
         "------------------------------------\n"

increase = 0.0

for year in range(YEARS):

    if year == 0:
        output += format(year + 1) + \
                  "\t$" + format(increase, '.2f') + \
                  "\t\t$" + format(variable_tuition, '.2f') + "\n"
    else: 
        increase = variable_tuition * TUITION_INCREASE

        variable_tuition = (variable_tuition * TUITION_INCREASE) + variable_tuition

        output += format(year + 1) +    \
                  "\t$" + format(increase, '.2f') + \
                  "\t\t$" + format(variable_tuition, '.2f') + "\n"

output += "------------------------------------\n"

print(output)

