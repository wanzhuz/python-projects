# mileage.py
# Wanzhu Zheng
#
# Calculates the gas mileage of each tank of fuel

print("Your Personal Fuel Economy")
total_miles = 0 # Calculates total miles traveled
total_gallons = 0 # Calculates total gallons
miles_traveled = 0

# Keeps asking the user for the total amount of miles traveled and gallons needed until prompted to stop
# Calculates total miles traveled and total gallons needed
while str(miles_traveled) > "":
    str_input = input("Number of miles traveled (or enter to exit):")

    # Breaks when user presses 'enter'
    if str_input == "":
        break
    miles_traveled = int(str_input)
    gallons_needed = int(input("Number of gallons needed:"))
    mileage_unr = miles_traveled / gallons_needed # Unrounded
    mileage_r = round(mileage_unr, 1) # Rounded

    print("Mileage this tank:", mileage_r)
    total_miles += miles_traveled
    total_gallons += gallons_needed

# Calculates average mileage
avg_mileage = total_miles / total_gallons
print("Average mileage:", round(avg_mileage,1))

