import random

print("here")

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 5

print("Pick a number between 1 and 50. You have 5 attempts to guess it.")

while attempts > 0:
    guess = input("Enter your guess: ")  # Get user input

    # Validate the input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number:", secret_number)
        break
    elif guess < secret_number:
        print("The number is higher than your guess.")
    else:
        print("The number is lower than your guess.")

    attempts -= 1
    print("You have", attempts, "attempts left.")
else:
    print("Sorry, you ran out of attempts. The correct number was:", secret_number)
