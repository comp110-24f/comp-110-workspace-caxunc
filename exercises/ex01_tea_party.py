__author__: str = "730753482"


"""
A function to compute the number of tea bags needed based on number of guests
A function to compute the number of treats needed based on the number of teas guests 
are expecting to drink
A function to compute the cost of the tea bags and the treats combined
Bringing these function together in a “main planner” function that calls each and 
produces printed output
Making the program runnable and asking a user for input when they run the program
"""


def tea_bags(people: int) -> int:
    """
    Calculate the number of teabags needed.
    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculates the number of treats needed based on the number of teas guests are
    expecting to drink.
    """
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculates the total cost of the tea party.
    """
    return 0.5 * tea_count + 0.75 * tea_count


def main_planner(guests: int) -> None:
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags:" + str(tea_bags(people=guests)))
    print("Treats:" + str(treats(guests)))
    print("Cost:$" + str(cost(tea_bags(guests), treats(guests))))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
