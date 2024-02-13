# find the maximum of 3 numbers

num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))
num_3 = int(input("Enter third number"))
# Maximum_of_three = max(num_1, num_2, num_3)
# print("Max number is ",Maximum_of_three)

if num_1 > num_2 > num_3:
    print("The max number is ", num_1)
elif num_2 > num_1 > num_3:
    print("The max number is ", num_2)
else:
    print("The max number is ",num_3)
    

