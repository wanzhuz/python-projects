# translate.py
#
# Wanzhu Zheng
# Takes the first consonant in a word, moves it to the back, and adds "-ay"
# If the word starts with a vowel, just add "way"

word = input("Enter a word to translate:")
word = word.lower() # changes it to lower case
vowels = "aeiou"

# checks if the word starts with a consonant
if word[0] in vowels:
    word += "way"
else:
    word = word[1:] + word[0] + "ay"

print("Pig latin:", word)
