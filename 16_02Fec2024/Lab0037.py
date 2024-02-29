# find the square root of list
import math


def square_root_of_number(num):
    return math.sqrt(num)


sq_list = [1, 2, 3, 4, 5, 6]
square_root = list(map(square_root_of_number, sq_list))
print("Square root of the number is :- ",square_root)

