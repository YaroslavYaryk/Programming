import time
import random
from pynput.keyboard import Controller

keyboard = Controller()  # Create the controller

def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 1)  # Generate a random number between 0 and 10
        time.sleep(delay)  # Sleep for the amount of seconds generated

type_string_with_delay("This is my string typed with a delay")
