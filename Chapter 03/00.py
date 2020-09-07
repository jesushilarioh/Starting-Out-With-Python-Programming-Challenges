# 7. Grade Calculator
#
# A class has two tests worth 25 points each along 
# with a main exam worth 50 points. For a student 
# to pass the class, they must obtain an overall 
# score of at least 50 points, and must obtain at 
# least 25 points in the main exam. If a student’s 
# total score is less than 50 or they obtain less 
# than 25 points in the main exam, they receive a 
# grade of “Fail”. Otherwise, their grade is as follows:
#
# If they get more than 80, they get a grade of 
# “Distinction”. 50–59 = “Pass”. If they get less 
# than 80 but more than 60, they get a “Credit” grade.
#
# If they get less than 60, they get a ”Pass” grade.
#
# Write a program that prompts the user to enter their 
# points for both tests and the exam and converts 
# the values to integers. The program should first 
# check if the points entered for the tests and exam 
# are valid. If any of the test scores are not between 
# 0 and 25, or the exam score is not between 0 and 50, 
# the program should display an error message. Otherwise, 
# the program should display the total points and the grade.

# 1. prompts the user to enter their 
#   points for both tests and the exam and converts 
#   the values to integers.
test_1_points = int(input("\nEnter points for test #1: "))

message = ""

if test_1_points >= 0 and test_1_points <= 25:
    test_2_points = int(input("Enter points for test #2: "))

    if test_2_points >= 0 and test_2_points <= 25:
        exam_points   = int(input("Enter points for exam   : "))
        
        if exam_points >= 0 and exam_points <= 50:
            total_points = test_1_points + test_2_points + exam_points

            if total_points < 50 or exam_points < 25:
                message = "FAIL"

            else:
                if total_points > 80:
                    message = "Distinction"
                elif total_points <= 80 and total_points >= 60:
                    message = "Credit"
                elif total_points < 60:
                    message = "Pass"

        else:
            message = "Invalid. Points for exam must be between 0 - 50."
    else:
        message = "Invalid. Points for test #2 must be between 0 - 25."
else:
    message = "Invalid. Points for test #1 must be between 0 - 25."

print(message)