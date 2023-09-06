# cash.py
#
# Wanzhu Zheng
# Returns the number of items and total price of the items in the file

print("Cash register")
file = input("Enter file of prices:")
infile = open(file)
count = 0 # number of items in the file
total = 0 # total price

# loops through the file
for line in infile:
    line = line.strip() # strips whitespace from ends
    num_ver = float(line) 

    total += num_ver 
    count += 1

print("File contained", count, "items totaling", "${:.2f}".format(total))
