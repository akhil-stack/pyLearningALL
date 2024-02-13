# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

triangle_side_1 = float(input("Enter the length of side 1"))
triangle_side_2 = float(input("Enter the length of side 2"))
triangle_side_3 = float(input("Enter the length of side 3"))

if triangle_side_1 == triangle_side_2 and triangle_side_2 == triangle_side_3:
    print("The Triangle is Equilateral")
elif triangle_side_1 != triangle_side_2 and triangle_side_1 == triangle_side_3:
    print("The Triangle is Isosceles")
else:
    print("The Triangle is Scale")

