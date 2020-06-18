def can_run_for_president(age, is_natural_born_citizen):
    """
    Можно ли балатироваться в президенты:
    Если меньше 35 лет - нельзя
    Если есть 35 и рожден в стране - можно
    Если есть 35 но не рожден в стране - нельзя
    """
    return age >= 35 and is_natural_born_citizen

def sign(x):
    """
    Returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def exactly_one_toping(ketchup, mustard, onion):
    """Return True if customer want exactly one of toppings"""
    return (ketchup + mustard + onion) == 1


