# 13. Shipping Charges
#
# The Fast Freight Shipping Company charges the following rates:
#
# Weight of Package                             Rate per Pound
# --------------------------------------------------------------
# 2 pounds or less                                  $1.50
# Over 2 pounds but not more than 6 pounds          $3.00
# Over 6 pounds but not more than 10 pounds         $4.00
# Over 10 pounds                                    $4.75
# --------------------------------------------------------------
#
# Write a program that asks the user to enter the weight of a 
# package then displays the shipping charges.

weight_of_package = float(input("Enter weight of package: "))
shipping_charges = 0.0

message = "Shipping charges = "

if weight_of_package <= 2:
    shipping_charges = weight_of_package * 1.50
elif weight_of_package > 2 and weight_of_package <= 6:
    shipping_charges = weight_of_package * 3.00
elif weight_of_package > 6 and weight_of_package <= 10:
    shipping_charges = weight_of_package * 4.00
elif weight_of_package > 10:
    shipping_charges = weight_of_package * 4.75

message += "$" + format(shipping_charges, ',.2f')

print(message)