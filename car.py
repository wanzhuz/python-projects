# car.py
# Wanzhu Zheng
#
# Prompts the user to guess the price of a car
# If they guess within 5 tries, they win, but there are unlimited guesses

print("Guess the price and win the prize!")
CAR_PRICE = 42500 # Sets car price
guess = 0
tries = 0

# Allows the user to keep guessing when their guess is not the car price
# Returns "You won the car!" if they guess correctly within 5 tries
# Returns "Too many guesses!" otherwise
while guess != CAR_PRICE:
    guess = int(input("Enter your guess:"))
    if guess > CAR_PRICE:
        print("Too high!")
        tries += 1
    elif guess < CAR_PRICE:
        print("Too low!")
        tries += 1
    elif guess == CAR_PRICE:
        if tries < 5:
            print("You won the car!")
        else:
            print("Too many guesses!")

