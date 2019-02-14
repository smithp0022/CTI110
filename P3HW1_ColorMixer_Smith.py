
# Color Mixer
# CTI-110 - P3HW1 - Color Mixer
# Patrick Smith
# 12 FEB 2019

# This program will give the user a secondary color
# when they enter two primary colors.

# define primary colors.

print("")
primary_color1 = input("Please enter first primary color: ")
primary_color2 = input("Please enter second primary color: ")

# define color mixture.

if (primary_color1 == "red") and (primary_color2 == "blue"):
    
# Display to the user the secondary color by mixing primary colors 1 and 2.

    print("\nYour color mixture is purple. ")
    
elif ( primary_color1 == "blue" and primary_color2 == "red" ):
    
# Display to the user the secondary color by mixing primary colors 1 and 2.

    print("\nYour color mixture is purple. ")

elif ( primary_color1 == "red" and primary_color2 == "yellow" ):

# Display to the user the secondary color by mixing primary colors 1 and 2.

    print("\nYour color mixture is orange. ")

elif ( primary_color1 == "yellow" and primary_color2 == "red" ):

# Display to the user the secondary color by mixing primary colors 1 and 2.

    print("\nYour color mixture is orange. ")

elif ( primary_color1 == "blue" and primary_color2 == "yellow" ):

# Display to the user the secondary color by mixing primary colors 1 and 2.

    print("\nYour color mixture is green. ")

elif ( primary_color1 == "yellow" and primary_color2 == "blue" ):

# Display to the user the secondary color by mixing primary colors 1 and 2.

    print("\nYour color mixture is green. ")
    
# if user does not enter a primary color display "error!"
else:
    print( "\nError! Your choices for primary color are: red, blue, or yellow" \
           " and you cannot select the same primary color twice.",sep="")

input("\nPress enter to exit.")

    



