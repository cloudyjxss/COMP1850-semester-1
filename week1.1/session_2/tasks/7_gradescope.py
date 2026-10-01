# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))

if number1.isdigit() == True and number2.isdigit() == True:
    result = number1*number2
    print(result)
else:
    print("That is not a number.")


# multiply those numbers together

# print out the result

# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!