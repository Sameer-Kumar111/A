# Python Question

# 1. Create a Variable to store the name and age of a student and print a formatted string.
# 2. Create a program that takes 2 numbers from the user and shows their addition, subtraction, multiplication, and division.
# 3. Write a program to check whether a number is even or odd using if-else.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
# 4. Take a number from the user and check if it is positive, negative, or zero.
# 5. Create a list of 5 fruits, Add a new fruit at the end and remove the second one.

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
fruits.append("Fig")  # Adding a new fruit at the end
fruits.pop(1)  # Removing the second fruit (index 1)
print(fruits)