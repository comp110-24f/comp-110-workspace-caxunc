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
    user_guess: str = input("Guess a number:")  # get a user input
    print("your guess was " + user_guess)  # print out the user input

    if int(user_guess) == secret:  # if the guessed value equals to 7.
        print("You got it!")

    if int(user_guess) < secret:  # if the guessed value is less than 7.
        print("Your guess was too low! The secret number is " + str(secret))

    if int(user_guess) > secret:  # if the guessed value is greater than 7
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()  # execute guess the number method.
