# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If, elif, else

mark_entered = float(input("Enter the Mark"))
if 90 <= mark_entered <= 100:
    print("Your grade is :- A")
elif 80 <= mark_entered <= 89:
    print("Your grade is :- B")
elif 70 <= mark_entered <= 69:
    print("Your grade is :- C")
elif 50 <= mark_entered <= 59:
    print("Your grade is :- D")
else:
    print("Invalid input")


