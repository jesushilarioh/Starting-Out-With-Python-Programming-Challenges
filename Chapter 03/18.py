message = ""

vegetarian = input("Is anyone in your party a vegetarian? ")

if vegetarian == "yes" or vegetarian == "no":
    vegan = input("Is anyone in your party a vegan? ")

    if vegan == "yes" or vegan == "no":
        gluten_free = input("Is anyone in your party gluten-free? ")

        if gluten_free == "yes" or gluten_free == "no":
            message = "\nHere are your restaurant choices:\n"

            if vegetarian == "yes":
                
                if vegan == "yes":

                    if gluten_free == "yes" or gluten_free == "no":
                        message += "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                else: 
                    if gluten_free == "yes":
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                    else:
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"
            else: # vegetarian == "no"

                if vegan == "yes":

                    if gluten_free == "yes" or gluten_free == "no":
                        message += "Corner Cafe\nThe Chef's Kitchen\n"

                else: # vegan == "no"

                    if gluten_free == "yes":
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                                   
                    else: # gluten free == "no"
                        message += "Joe's Gourmet Burgers\n" + \
                                   "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"

        else:
            message = "Enter either 'yes' or 'no'.\nRerun the program and try again."
    
    else:
        message = "Enter either 'yes' or 'no'.\nRerun the program and try again."

else:
    message = "Enter either 'yes' or 'no'.\nRerun the program and try again."


print(message)