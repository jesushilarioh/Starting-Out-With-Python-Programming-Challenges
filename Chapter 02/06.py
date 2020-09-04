# Receive
purchase_amount = float(input('Enter the amount of purchase: $'))
number_of_installments = int(input('Enter number of payment installments: '))

PERCENTAGE = .05

# Calculate
total_purchase_amount = (purchase_amount * PERCENTAGE) + purchase_amount
installment_amount = total_purchase_amount / number_of_installments

# Display                              200,000,000.02
print('\nPurchase amount = $', format(purchase_amount, ',.2f'), sep='')
print('Number of installments =', number_of_installments)
print('Total purchase amount = $', format(total_purchase_amount, ',.2f'), sep='')
print('Installment amount = $', format(installment_amount, ',.2f'), sep='', end='\n\n')