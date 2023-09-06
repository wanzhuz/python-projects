# ticket.py
# Wanzhu Zheng
#
# Returns the ticket price for each person depending on age

age = int(input("Enter age:")) # Gets the age of the person

# Returns the price for children ages 3 to 12
while age <= 12:
    if age <=3:
        print("Price: FREE")
        break
    else:
        print("Price: $29.95")
        break

# Returns the price for students
while age > 12 and age < 65:
    if age <= 17:
        print("Price: $39.95")
        break
    elif age > 17:
        college_id = input("College ID? (y/n)")
        if college_id == "y":
            print("Price: $39.95")
            break
        else:
            print("Price: $49.95")
            break

# Returns the price for seniors
while age >= 65:
    print("Price: $39.95")
    break
    
    
