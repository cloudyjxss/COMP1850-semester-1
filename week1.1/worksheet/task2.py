"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jess Collier
"""


name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


try:
    SaveAmount = int(input("How much do you want to save every month? "))
    TotalSaved = SaveAmount * 12
    print(f"You will have saved £{TotalSaved:.2f} by the end of the year.")
    InterestAndTotalSaved = TotalSaved * 1.008
    print(f"The total saved including interest is £{InterestAndTotalSaved:.2f}.")
except:
    print("Invalid amount")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.




# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).



