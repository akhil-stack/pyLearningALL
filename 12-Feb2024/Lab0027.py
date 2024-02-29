# Fibonacci series
# 0 1 1 2 3 5 8

Limit = int(input("Enter the limit for Series"))
a, b = 0, 1
while a < Limit:
    print(a, end=" ")
    a, b = b, a + b


