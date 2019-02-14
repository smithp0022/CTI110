
# CTI-110 P3T1 - Areas of Rectangles
# Patrick Smith
# 12 FEB 2019

print("")

print("This program calculates the area diffference between two rectangles.")

# Input the length and width of rectangle 1.

length1 = float(input("\nEnter the length of rectangle 1: "))

width1 = float(input("Enter the width of rectangle 1: "))

# Input the length and width of rectangle 2.

length2 = float(input("\nEnter the length of rectangle 2: "))

width2 = float(input("Enter the width of rectangle 2: "))

# Calculate the area of rectangle 1.

area1 = length1 * width1

# Calculate the area of rectangle 2.

area2 = length2 * width2

# Determine which has the greater area.

if area1 > area2:
    print("\nRectangle 1 has the greatest area.")

else:
    if area2 > area1:
        print("\nRectangle 2 has the greatest area.")

    else:
        print("\nBoth rectangles have the same area.")

input("\nPress Enter to exit.")
