
# CTI-110 Letter Grade Program
# 13 FEB 2019
# Patrick Smith
# This program takes a number grade and outputs a letter grade.

print("")

# system uses 10-point grading scale.

def main():
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

# TO DO: define the rest of the scores.

A_score = "90"
B_score = "80"
C_score = "70"
D_score = "60"

# Ask the user to enter the numerical value.

score = input("Enter grade: ")

# display output of numerical value to letter grade.

if score >= A_score:
    print("Your grade is: A.")
else:
    if score >= B_score:
        print("Your grade is: B.")
    else:
        if score >= C_score:
            print("Your grade is: C.")
        else:
            if score >= D_score:
                print("Your grade is: D.")
            else:
                print("Your grade is: F.")

# TO DO: finish this
# program start
main()

input("\nPress Enter key to exit.")
