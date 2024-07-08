# The Greatest Showdown

# Task 1: Identify the Greatest

# Prompt the user to enter three numbers
num1 = float(input("Enter the first nubmer: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Identify the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num3
else:
    largest = num3

# Print the largest number
print("The largest number is: ", largest)


# Task 2: Identify the smallest
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Print the smallest number
print("The smallest number is: ", smallest)