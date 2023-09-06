# roth.py
# Wanzhu Zheng
#
# Calculates the number of months needed for an investment to double

initial_investment = float(input("Enter an initial Roth IRA deposit amount:"))
apr = float(input("Enter an annual percent rate of return:"))

DIVIDEND = apr / 100 # Sets the monthly dividend amount
end_returns = 0
current_value = initial_investment
month = 1

# Counts the number of full months needed for investment to double
# Calculates the returns after each month
while end_returns < 2 * initial_investment:
    end_returns = current_value + current_value * DIVIDEND / 12
    current_value = end_returns

    print("Value after month", str(month) + ":", "${:.2f}".format(end_returns))
    month += 1

print("It will take", month - 1, "months to double your investment with a", "{:.0f}%".format(apr), "return.")
    
 
