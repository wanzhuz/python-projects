# cash2.py
#
# Wanzhu Zheng
# Removes special characters and skips over any line that cannot be converted to a float

print("Cash register")
file = input("Enter file of prices:")
infile = open(file)
count = 0
total = 0
num_ver = 0
new_str = ""

# loops through the file
for line in infile:
    new_str = line.strip("$")
    # skips over unconvertable strings
    # removes any special characters
    try:
        num_ver = float(new_str)
        count += 1
        total += num_ver
    except ValueError:
        continue
        
print("File contained", count, "items totaling", "${:.2f}".format(total))

