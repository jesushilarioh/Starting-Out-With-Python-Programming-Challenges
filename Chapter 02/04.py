SALES_TAX = .07

item1 = float(input('\nEnter the price for item 1 $'))
item2 = float(input('Enter the price for item 2 $'))
item3 = float(input('Enter the price for item 3 $'))
item4 = float(input('Enter the price for item 4 $'))
item5 = float(input('Enter the price for item 5 $'))

subtotal =  float(item1 + item2 + item3 + \
                  item4 + item5)

total_sales_tax = subtotal * SALES_TAX

total = subtotal + total_sales_tax
#3,000,000.09
print('\nTotal = $', format(total, ',.2f'), sep='', end='\n\n')