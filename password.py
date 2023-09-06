# password.py
#
# Wanzhu Zheng
# Asks the user for a password and returns the length and properties of the password

password = input("Enter password:")
length = 0
lower_case = False
upper_case = False
has_digit = False
has_special = False

# loops over each letter in the password
for letter in password:
    # counts the length
    length += 1
    # determines whether there are lower case letters
    if letter.islower():
        lower_case = True
    # determines whether there are upper case letters
    if letter.isupper():
        upper_case = True
    # determines whether there are digits
    if letter in "0123456789":
        has_digit = True
    # determines whether there are special characters
    if letter in "@#$*!":
        has_special = True 
    
print("Length:", length)
if lower_case == True:
    print("Has lower case")
if upper_case == True:
    print("Has upper case")
if has_digit == True:
    print("Has digit")
if has_special == True:
    print("Has special")

