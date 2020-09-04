# 1. Input (receive info)
charge_for_food = float(input('\nEnter charge for food: $'))

# 2. Process (calculate info)
TIP_PERCENTAGE = .18
SALES_TAX = .07

tip = (charge_for_food * TIP_PERCENTAGE)
sales_tax = (charge_for_food * SALES_TAX)
grand_total = charge_for_food + tip + sales_tax

# 3. Output (display info) 7,809,349,394.93
print('\nCharge for food = $', format(charge_for_food, ',.2f'), sep='')
#Charge for food = $----9,9384.00
print('Tip = $', format(tip, ',.2f'), sep='')
print('Sales tax = $', format(sales_tax, ',.2f'), sep='')
print('Grand total = $', format(grand_total, ',.2f'), sep='', end='\n\n')