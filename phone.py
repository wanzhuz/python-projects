# phone.py
#
# Wanzhu Zheng
# Print "Valid" if the phone number is in the form ###-###-####, otherwise print "Invalid"

phone_number = input("Enter number as  ###-###-####:")
valid = True 
pos = 0 # position of the iterator

# runs the loop when the phone number is valid and the position is less than 12
while valid and pos < 12:
    if pos == 3:
        valid = phone_number[pos] == "-"
    elif pos == 7:
        valid = phone_number[pos] == "-"
    else:
        valid = phone_number[pos].isdigit()
    pos += 1

if valid:
    print("Valid")
else:
    print("Invalid")
    
        
    
