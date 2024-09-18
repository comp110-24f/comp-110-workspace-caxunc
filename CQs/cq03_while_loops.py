"""
While loops challenging questions.
"""

__author__ = "730853482"

def num_instances(phrase: str, search: str) -> int:
    """
    Given a phrase and a letter to search for, this method 
    returns the number of instances which it occurs. 
    
    """
    count: int = 0  # initalise the count to 0.
    index: int = 0  # initalize the index to 0 because we start at 0.
    
    while(index < len(phrase)): # loop through through the letters of the index.
        if(phrase[index] == search): # Test whether the letter at the index matches the letter given.
            count += 1 # increase counter by 1 if the letter matches. 

    return count # return the number of counts.
