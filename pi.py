# pi.py
# Wanzhu Zheng
#
# Approximates the value of pi from an infinite series up to N terms and calculates error
import math

UPPER_BOUND = int(input("Number of terms:")) # Sets upper bound of sequence
iter_var = 0 # The lower bound and also the iteration constant
quarter_pi_approx = 0
error = 0

# Parses through the Leibniz formula for pi until the upper bound
# Only gives value of pi / 4
while iter_var < UPPER_BOUND:
    quarter_pi_approx += ((-1) ** iter_var) / (2 * iter_var + 1)
    iter_var += 1

pi_approx = 4 * quarter_pi_approx # Approximates value of pi

# Calculates error of approximation
error = math.pi - pi_approx

print("Estimate of pi:", f"{pi_approx:.10f}")
print("Error:", f"{error:.10f}")
