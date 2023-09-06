# parrot.py
#
# Wanzhu Zheng
# Returns a capitalized version of what the user has wrote until "hush"

# While the word the user puts is not "hush", return a capitalized version
# Otherwise, exit the program
while True:   
    str_input = input(">") # Gets the user input

    # Makes sure that the indefinite loop is exited regardless of capitalization
    if str_input.lower() == "hush":
        break
    # Returns capitalized version
    else:
        cap_version = str_input.upper()
        print(cap_version)
    

