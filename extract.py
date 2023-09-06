# extract.py
#
# Wanzhu Zheng
# Takes away any special characters and saves only the numbers

phone = input("Enter phone number: ")
only_numbers = ""
missing = "()- " # takes out these symbols

# loops through the phone number
for pos in phone:
    # checks whether any iteration has a symbol
    if pos in missing:
        pos = ""
    only_numbers += pos

print("Numbers:", only_numbers)
