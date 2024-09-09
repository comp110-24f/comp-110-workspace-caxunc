"""
A function to compute the number of tea bags needed based on number of guests
A function to compute the cost of the tea bags and the treats combined
Making the program runnable and asking a user for input when they run the program
"""

__author__: str = "730753482"


def tea_bags(people: int) -> int:
    """
    Calculate the number of teabags needed.
    """
    return people * 2 #return the total number of teabags.


def treats(people: int) -> int:
    """
    Calculates the number of treats needed based on the number of teas guests are
    expecting to drink.
    """
    return int(tea_bags(people=people) * 1.5) # returns the total number of treats using the number of people.


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculates the total cost of the tea party.
    """
    return 0.5 * tea_count + 0.75 * treat_count #return the total costs of the tea and treats by multiplying number of items with their corresponding costs.


def main_planner(guests: int) -> None:
    """
    Print the statements
    """
    print("A Cozy Tea Party for " + str(guests) + " People!") #print the number of guests.
    print("Tea Bags: " + str(tea_bags(people=guests)))#print the number of tea bags.
    print("Treats: " + str(treats(guests)))#print the number of treats.
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))#prints the total costs of the tea party.



if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? "))) #run the main method.
