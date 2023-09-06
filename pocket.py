# pocket.py
# Wanzhu Zheng
#
# Converts a total value from quarters, dimes, nickels, and pennies to dollars and cents

print("Pocket change calculator")
quarter_num = int(input("How many quarters?")) # Number of quarters
dime_num = int(input("How many dimes?")) # Number of dimes
nickel_num = int(input("How many nickels?")) # Number of nickels
penny_num = int(input("How many pennies?")) # Number of pennies

# Converts number of coins to money
quarter_amount = quarter_num * 0.25
dime_amount = dime_num * 0.1
nickel_amount = nickel_num * 0.05
penny_amount = penny_num * 0.01

# Adds for total cents
total_cents = quarter_amount + dime_amount + nickel_amount + penny_amount

# Returns the amount in dollars and cents
formatted_str = "${:.2f}".format(total_cents)
print("You have", formatted_str)
