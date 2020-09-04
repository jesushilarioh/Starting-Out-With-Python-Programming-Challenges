#1. Input
number_of_males = int(input('Enter the number of males: '))
number_of_females = int(input('Enter the number of females: '))

#2. Process
total_number_of_students = number_of_females + number_of_males
percentage_of_males = number_of_males / total_number_of_students
percentage_of_females = number_of_females / total_number_of_students

#3. Output
print('Total number of males =', format(percentage_of_males, '.0%'))
print('Total number of females =', format(percentage_of_females, '.0%'))