SIZE = 7

output = "\n"

for row in range(SIZE):
    output += "#"

    for column in range(row):
        output += " "
    
    output += "#\n"

print(output)