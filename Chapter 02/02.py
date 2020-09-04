PROFIT_PERCENTAGE = .25

total_sales = float(input('\nEnter projected total sales amout: $'))

annual_profit = total_sales * PROFIT_PERCENTAGE

print('Total profit made = $' + format(annual_profit, ',.2f') + '\n') #1000.90