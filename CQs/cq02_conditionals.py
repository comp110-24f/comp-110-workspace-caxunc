"""
A function that allows the user to guess a random number through the user input and 
will produce a response on whether it is right or not. 
"""

__author__: str = "730753452"


def guess_a_number() -> None:
    """
    A function which takes no input and does what is said in the docstring.
    """
    secret: int = 7  # declare a secret number and it is equal to 7
    guessed: str = input("Guess a number: ")  # get a user input
    print("your guess was " + guessed)  # print out the user input

    if int(guessed) == 7:  # if the guessed value equals to 7.
        print("You got it!")

    elif int(guessed) < 7:  # if the guessed value is less than 7.
        print("Your guess was too low! The secret number is " + str(secret))

    elif int(guessed) > 7:  # if the guessed value is greater than 7
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "main":
    guess_a_number()  # execute guess the number method.
