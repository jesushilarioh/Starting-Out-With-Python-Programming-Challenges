ONE_POUND_IN_KILOGRAMS = .454

object_mass_pounds = float(input('\nEnter mass of an object: ')) # 3.4

object_mass_kilograms = object_mass_pounds * ONE_POUND_IN_KILOGRAMS

print('Object in kilograms =', format(object_mass_kilograms, ',.2f'), end='\n\n') # 1434500.90