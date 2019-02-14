
# Meal Tip Tax Calculator
# 12 FEB 2019
# CTI-110 P3HW2 - Meal Tip Tax Calculator
# Patrick Smith

print("")

# input the total meal amount in $.

meal_amount = float(input("Enter the meal amount: $"))

# Ask the user to provide tip amount in 15, 18 , or 20.

tip_amount = input("What amount of tip do you wish to consider?: ")

# Define tip variables.

tip_1 = "15"
tip_2 = "18"
tip_3 = "20"

# Calculate the sales tax .07

tax = meal_amount * .07


# Calculate the tip using meal_amount* 0.15, 0.18, & 0.20.

tip_amount1 = meal_amount * .15
tip_amount2 = meal_amount * .18
tip_amount3 = meal_amount * .20

# Calculate the total cost of the meal_amount plus the tip_amount

total_cost1 = meal_amount + tax + tip_amount1
total_cost2 = meal_amount + tax + tip_amount2
total_cost3 = meal_amount + tax + tip_amount3


# Display all totals for a meal.

if tip_amount == tip_1:
    print("\nMeal amount is: $",format(meal_amount,",.2f"),sep="")
    print("15% is $",format(tip_amount1,",.2f"),sep="")
    print("tax is $",format(tax,".2f"),sep="")
    print("total meal cost is $", format(total_cost1, ",.2f"),sep="")

elif tip_amount == tip_2:
    print("\nMeal amount is: $",format(meal_amount,",.2f"),sep="")
    print("18% is $", format(tip_amount2,",.2f"),sep="")
    print("tax is $",format(tax,".2f"),sep="")
    print("total meal cost is $", format(total_cost2, ",.2f"),sep="")

elif tip_amount == tip_3:
    print("\nMeal amount is: $",format(meal_amount,",.2f"),sep="")
    print("20% is $", format(tip_amount3,",.2f"),sep="")
    print("tax is $",format(tax,".2f"),sep="")
    print("total meal cost is $", format(total_cost3, ",.2f"),sep="")

# Error message if other than 15%, 18%, or 20% is entered.

else:
    print( "\nError! You must choose 15%, 18%, or 20% only!" )

input("\nPress the 'Enter Key' to exit.")
