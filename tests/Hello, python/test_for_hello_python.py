from hello_python import *

#TEST FOR ARITHMETIC OPERATIONS
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplycation(a, b):
    return a * b
def true_division(a, b):
    return a / b
def floor_division(a, b):
    return a // b
def modulus(a, b):
    return a % b
def exponentiation(a, b):
    return a ** b
def negation(a):
    return - a

# TEST FOR DEFINING AREA OF CIRCLE
def area_circle():
    pi = 3.14159  # approximate
    print("Введите значение диаметра", )
    diameter = int(input())
    radius = diameter / 2
    area = pi * (radius **2)
    return area

# TEST FOR SWAP VARIABLE
def swap_variable(a, b):
    a, b = b, a
    return a, b

#FOR THE SAKE OF THEIR FRIENDSHIP
def candies_to_smash():
    alice_candies, bob_candies, carol_candies = int(input()), int(input()), int(input())
    to_smash = (alice_candies + bob_candies + carol_candies) % 3
    return to_smash




