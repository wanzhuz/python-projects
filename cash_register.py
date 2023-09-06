# statistics.py
# Wanzhu Zheng
#
# Asks the user for the price of each item purchased
# Returns with a statement including the total number of items and total price

print("Cash register")
running_count = 0 # Number of items entered for now
running_sum = 0 # Sum of item values for now

# Calculates the sum of the values and the number of items entered
while True:
    str_input = input("Enter the price of an item:") # Value in string
    
    # Breaks out of the loop if the user doesn't enter a number
    if str_input == "":
        break

    value = float(str_input) # Converts value to float
    
    running_count += 1
    running_sum += value

print("You entered", running_count, "items totaling", "${:.2f}".format(running_sum))

