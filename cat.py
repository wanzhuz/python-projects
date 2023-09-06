# cat.py and trycat.py
#
# Wanzhu Zheng
# Use try and except to prompt the user to enter a valid file


# asks user indefinitely until valid input is made
while True:
    try:
        file = input("Enter a file name to open:")
        infile = open(file) # opens the file

        # loops through the file
        for line in infile:
            line = line.strip() # strips whitespace from the ends
            print(line)
        break
        
    except FileNotFoundError:
        print("Could not open", file)
        continue
        


