# tip.py
# Wanzhu Zheng
#
# Outputs a range of tips from 15% to 25% based on customer satisfaction

total_bill = float(input("Enter total bill:")) # Total bill amount
iter_var = 15 # Sets an interation variable for the while loop

# Returns the tip that should be payed based on the total bill
# 15% for mediocre to 25% for great service
while iter_var >= 15 and iter_var <= 25:
    tip = iter_var / 100 * total_bill # Returns tip
    print("{:.0f}%".format(iter_var), "is", "${:.2f}".format(tip))
    iter_var += 1

