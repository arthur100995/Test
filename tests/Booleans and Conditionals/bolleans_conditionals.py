# Ex 1
# def sign(x):
#     if x > 0:
#         return 1
#     elif x < 0:
#         return -1
#     else:
#         return 0


# Ex 2
# def to_smash(total_candies, total_friends=3):
#     if total_candies != 1:
#         print("Splitting", total_candies, "candies")
#         return total_candies % 3
#     else:
#         print("Splitting 1 candy")
#         return total_candies
# print(to_smash(1))



# EX 3
# def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
#     # Don't change this code. Our goal is just to find the bug, not fix it!
#     return have_umbrella or (rain_level < 5 and have_hood) or (not (rain_level > 0 and is_workday))
#
# # Change the values of these inputs so they represent a case where prepared_for_weather
# # returns the wrong answer.
# have_umbrella = False
# rain_level = 0.0
# have_hood = False
# is_workday = False
#
# # Check what the function returns given the current values of the variables above
# actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
# print(actual)

# EX 4
