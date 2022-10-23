number = 0
total = 0

while number >= 0:
    
    number = int(input("Enter a positive number: "))

    if number >= 0:
        total += number 

output = "Total = " + format(total)

print(output)
