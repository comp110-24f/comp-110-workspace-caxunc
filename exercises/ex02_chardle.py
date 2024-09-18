"""EX02 - Charcle - A cute step toward Wordle."""

__author__: str = "730753482"


def input_word() -> str:
    """
    This is a funciton that would get a five letter word from the user, and returns
    an error if the input is not.
    """
    word: str = input("Enter a 5-character word: ")  # Get input from user.

    if len(word) < 5 or len(word) > 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Test for the length of the word, and exits if it is not five.
    return word


def input_letter() -> str:
    """
    This is a function that gets a letter fromt eh user, and returns an error if
    the input is not.
    """
    character: str = input("Enter a single character:")  # Gets input from user.

    if len(character) > 1:
        print("Error: Character must be a single character.")
        exit()  # Test fro the length of the word, and exists if it is not.
    return character


def contains_char(word: str, letter: str) -> None:
    """
    This is a function which checks whther the letter chosen is within the word given,
    and if the letter is in the word, it would return it's index.
    """
    print("Searching for " + letter + " in " + word)
    count = 0  # keep counts of all number of instances which the letter appears.
    if word[0] == letter:
        print(letter + " found at index " + str(0))
        count += 1
    if word[1] == letter:
        print(letter + " found at index " + str(1))
        count += 1
    if word[2] == letter:
        print(letter + " found at index " + str(2))
        count += 1
    if word[3] == letter:
        print(letter + " found at index " + str(3))
        count += 1
    if word[4] == letter:
        print(letter + " found at index " + str(4))
        count += 1

    if count == 0:  # returns "no instances" found if count is 0, "instance" when count
        # is 1, and print the count for the rest.
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1" + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:  # the main method that would run when one excute the program.
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
