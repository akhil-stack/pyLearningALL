# Program to check a given number is leap year or not
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

Year = int(input("Enter the Year to check:-"))
if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print("The entered year",Year, "is a Leap year")
else:
    print("The Entered year",Year," is not a leap year")
