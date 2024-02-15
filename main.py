from pyscript import document
from js import document, CustomEvent
import random

def generateRandomNumber():
    return random.randint(1, 50)

randomNumber = generateRandomNumber()
numberOfTriesLeft = 5
print("random number -> ", randomNumber)
print("numberOfTriesLeft -> ", numberOfTriesLeft)
triesOutput = document.querySelector("#tries")
# triesOutput.innerText = "Number of tries left:  {}".format(numberOfTriesLeft)


def handleSubmit(event):
    global numberOfTriesLeft
    numberOfTriesLeft -=1
    triesOutput.innerText = "Number of tries left:  {}".format(numberOfTriesLeft)
    print("numberOfTriesLeft -> ", numberOfTriesLeft)
    input_text = document.querySelector("#inputNumber")
    input_value = input_text.value.strip()

    # Check if input_value is a valid number between 1 and 50
    if not input_value.isdigit() or not 1 <= int(input_value) <= 50:
        document.querySelector("#output").innerText = "Please enter a valid number between 1 and 50."
        return

    inputtedNumber = int(input_value)
    print("inputtedNumber -> ", inputtedNumber)

    output_div = document.querySelector("#output")

    if inputtedNumber == randomNumber:
        output_div.innerText = "Correct Answer!"
        output_div.classList.add("correct-answer")  # Add a class name to indicate correct answer

    elif numberOfTriesLeft == 0:
        output_div.innerText = "You ran out of tries! The correct answer was {}".format(randomNumber)
        triesOutput.classList.add("out-of-tries")
        document.dispatchEvent(CustomEvent.new("outOfTries"))
    elif inputtedNumber > randomNumber:
        output_div.innerText = "Too high"
    else:
        output_div.innerText = "Too low"
