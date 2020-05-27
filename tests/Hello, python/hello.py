def add_func(a, b):
    return round((a + b), 2)

def true_division(a, b):
    return round((a / b), 2)

def exponantional_to(a, b):
    return a ** b

def exchange_values(a, b):
    return b, a

def candies_to_smash(alice, bob, carol):
    return round(
        (alice+bob+carol) % 3, 2
    )