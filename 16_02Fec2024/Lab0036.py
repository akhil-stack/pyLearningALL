# find the sq: of a list by using map function

def square_of_number(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5, 6]
sq_number = list(map(square_of_number,numbers))
print(sq_number)

