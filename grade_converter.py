# FILE NAME - grade_converter.py

# NAME: Robert Young
# DATE: 02/28/2026
# BRIEF DESCRIPTION:  Create code that converts a numerical grade to a letter grade.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    def convert_grader():
        print("===== Grade Converter =====")
        grade = int(input("Enter a numerical grade (1-100): "))
        if grade < 65:
                print("F")
        elif grade >= 65 and grade < 70:
                print("D")
        elif grade >= 70 and grade < 80:
                print("C")
        elif grade >= 80 and grade < 90:
                print("B")
        elif grade >= 90 and grade <= 100:
                print("A")
        else:
                print("A+")
                   
    convert_grader()
main()
########### END YER CODE ABOVE THIS LINE ###########

########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
For me, I would say I had to verify the tab indent was in the correct location

'''
