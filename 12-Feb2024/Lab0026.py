# Factorial
# N! = n*(n-1)!
number = int(input("Enter the number\n"))
if number < 0:
    print("Invalid entry")
elif number == 0:
    print("Factorial is 1")
else:
    fact = 1
    for i in range(1, number + 1):
        fact = i * fact

print("Factorial of the number is ", fact)
