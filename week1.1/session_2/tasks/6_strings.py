# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #extra blank line at the start
print(f"Modified String 1: {user_string.lower()}") #lower case
print(f"Modified String 2: {user_string.upper()}") #upper case
print(f"Modified String 3: {user_string.strip()}") 
print(f"Modified String 4: {user_string.replace('a', '@')}") #replace a with @
print(f"Modified String 5: {user_string.capitalize()}") #first letter upper case
print(f"Modified String 6: {user_string[::-1]}") #prints the last letter
print(f"Modified String 7: {user_string.title()}")
print(f"Modified String 8: {len(user_string)}") #prints the number of characters inn the string
print(f"Modified String 9: {user_string.find('a')}") #finds position of a
print(f"Modified String 10: {user_string.count('a')}") #finds the number of a
print(f"Modified String 11: {user_string.startswith('Hello')}") #prints words that start with Hello
print(f"Modified String 12: {user_string.endswith('!')}")#prints words that end with !
print(f"Modified String 13: {user_string.isalnum()}") #true if its an alpha numeric
print(f"Modified String 14: {user_string.isalpha()}") # true if all characters are in the alphabet
print(f"Modified String 15: {user_string.isdigit()}") # true if integer



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!