SIZE = 8

output = "\n"

for row in range(SIZE, 0, -1):

    for column in range(row):

        output += "#"

    output += "\n"

print(output)