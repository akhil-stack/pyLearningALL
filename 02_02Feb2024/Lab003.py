# Task 2: Print the Table of 2 by using the command print()
import keyword

num = int(input("Enter the value which table needs to be generated:- "))
for count in range(1, 11):
    print(num, 'X', count, '=', num * count)

print(keyword.kwlist)
