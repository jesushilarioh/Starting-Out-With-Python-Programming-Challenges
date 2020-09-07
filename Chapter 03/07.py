message = ""

test_1_points = int(input("\nEnter points for test #1: "))

if test_1_points >= 0 and test_1_points <= 25:
    test_2_points = int(input("\nEnter points for test #2: "))

    if test_2_points >= 0 and test_2_points <= 25:
        exam_points   = int(input("Enter points for exam   : "))

        if exam_points >= 0 and exam_points <= 50:
            total_points = test_1_points + test_2_points + exam_points

            if total_points < 50 or exam_points < 25:
                message = "FAIL."
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