# Import neccessary dependencies
from pyscript import document
from js import document, CustomEvent
import random

# Declare function that generates a random number when we call it
def generateRandomNumber():
    return random.randint(1, 50)

# Call this function and hold the result in the randomNumber variable
# Declare a new variable called numberOfTriesLeft and set it to 5
# Log out to console to double check code is working
randomNumber = generateRandomNumber()
numberOfTriesLeft = 5
print("random number -> ", randomNumber)
print("numberOfTriesLeft -> ", numberOfTriesLeft)
# Get the output field with the id of "tries" and assign it to triesOutput
triesOutput = document.querySelector("#tries")

# Declare new function to handle the submit click
# - Remove one from the number of tries
# - Ensure input is valid
# - Check if input is equal, higher than, or less than the random number
def handleSubmit(event):
    global numberOfTriesLeft
    numberOfTriesLeft -=1
    triesOutput.innerText = "Number of tries left:  {}".format(numberOfTriesLeft)
    print("numberOfTriesLeft -> ", numberOfTriesLeft)
    input_text = document.querySelector("#inputNumber")
    input_value = input_text.value.strip()

    if not input_value.isdigit() or not 1 <= int(input_value) <= 50:
        document.querySelector("#output").innerText = "Please enter a valid number between 1 and 50."
        return

    inputtedNumber = int(input_value)
    print("inputtedNumber -> ", inputtedNumber)

    output_div = document.querySelector("#output")

    if inputtedNumber == randomNumber:
        output_div.innerText = "Correct Answer!"
        output_div.classList.add("correct-answer")
    elif numberOfTriesLeft == 0:
        output_div.innerText = "You ran out of tries! The correct answer was {}".format(randomNumber)
        triesOutput.classList.add("out-of-tries")
        document.dispatchEvent(CustomEvent.new("outOfTries"))
    elif inputtedNumber > randomNumber:
        output_div.innerText = "Too high"
    else:
        output_div.innerText = "Too low"
