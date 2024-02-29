# filter

# def even(number):
#     return number % 2 == 0
#
#
number = [1, 2, 3, 4, 5, 6]
# even_list = list(filter(even,List))
even_number = filter(lambda item: item % 2 == 0, number)
print(even_number)
