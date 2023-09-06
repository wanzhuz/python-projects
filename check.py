# check.py
#
# Wanzhu Zheng
# Checks whether the card number is valid or invalid and returns the check digit if invalid
import math

card = input("Enter your 8-digit card number:")
num_card = int(card.replace(" ", ""))
repl = num_card
excl_last = 0
check_digit = 0
even_digit = 0
even_sum = 0
odd_sum = 0
total_sum = 0

# digits in card decreases
# loops through the card for the numbers in odd positions
while num_card > 0:
   odd_sum += num_card % 10
   num_card = num_card // 100
# loops through the card for the numbers in even positions
while repl > 0:
    even_digit = 2 * (repl % 100 // 10)
    # if the digit is greater than 9, split it up and add
    if even_digit > 9:
        even_digit = even_digit // 10 + even_digit % 10
    else:
        even_digit = even_digit
    even_sum += even_digit
    repl = repl // 100
    
total_sum = even_sum + odd_sum
# returns valid if the total ends in 0
if total_sum % 10 == 0:
   print("Valid")
else:
   # finds the check digit
   excl_last = total_sum - int(card[-1])
   check_digit = (math.ceil(excl_last / 10) * 10) - excl_last
   print("Invalid")
   print("Check digit should be", check_digit)
    
