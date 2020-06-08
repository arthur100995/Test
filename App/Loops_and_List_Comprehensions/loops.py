import numpy as np
import random



def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky.
    A lucky list contains at least one number divisible by 7."""
    return any([num % 7 == 0 for num in nums])

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise."""
    n_number = []
    for num in L:
        n_number.append(num > thresh)
    return n_number

def elementwise_greater_than_two(L, thresh):
    """Second version elementwise_greater_than"""
    n_number = [num > thresh for num in L]
    return n_number

def menu_is_boring(meals):
    """Given a list of meals served over some period of time,
       return True if the same meal has ever been served two days in a row,
       and False otherwise."""
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False






