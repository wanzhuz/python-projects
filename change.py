# change.py
# Wanzhu Zheng
#
# Returns the minimum number of coins that can be converted from total change

total_cents = int(input("Enter change:")) # Gets the total change from user
total_quarters = total_cents // 25 # Outputs maximum number of quarters
total_dimes = (total_cents % 25) // 10 # Outputs maximum number of dimes
total_nickels = (total_cents % 25 % 10) // 5 # Outputs maximum number of nickels
total_pennies = total_cents % 25 % 10 % 5 # Outputs maximum number of pennies

print("Quarters:", total_quarters)
print("Dimes:", total_dimes)
print("Nickels:", total_nickels)
print("Pennies:", total_pennies)




