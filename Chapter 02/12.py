STOCKBROKER_COMMISSION = .03

shares_sold = shares_purchased = 2000
price_per_share = 40.00

amount_paid_for_stock = shares_purchased * price_per_share
print('\nAmount of money paid for the stock = $', 
       format(amount_paid_for_stock, ',.2f'), 
       sep='')

commission_paid_when_bought = amount_paid_for_stock * STOCKBROKER_COMMISSION
print('Amount of commission paid to broker when Joe bought the stock = $', 
       format(commission_paid_when_bought, ',.2f'),
       sep='')

price_per_share = 42.75

amount_stock_sold_for = shares_sold * price_per_share
print('Amount for which Joe sold the stock = $', 
       format(amount_stock_sold_for, ',.2f'),
       sep='')

commission_paid_when_sold = amount_stock_sold_for * STOCKBROKER_COMMISSION
print('Amount of commission paid to broker when Joe sold the stock = $',
       format(commission_paid_when_sold, ',.2f'),
       sep='')

total_amount_left = amount_stock_sold_for - \
                   (commission_paid_when_bought + \
                    commission_paid_when_sold)

print('\nTotal leftover =', 
      format(total_amount_left, ',.2f'), 
      '\nJoe made a profit.\n')