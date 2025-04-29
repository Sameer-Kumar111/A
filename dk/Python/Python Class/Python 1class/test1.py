# 1. Create a Variable to store the name and age of a student and print a formatted string.

name = "John Doe"
age = 20

# Printing a formatted string
print(f"The student's name is {name} and their age is {age}.")



# 2. Create a program that takes 2 numbers from the user and shows their addition, subtraction, multiplication, and division.
# Taking two numbers as input from the user
num1 = 5
num2 = 5

# Performing operations and displaying results
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division: Cannot divide by zero")
    
    
    
# 3. Write a program to check whether a number is even or odd using if-else.



number = 2
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
    
    
    
# 4. Take a number from the user and check if it is positive, negative, or zero.
number = 5
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")
    
    
  
  
# 5. Create a list of 5 fruits, Add a new fruit at the end and remove the second one.

# Create a list of 5 fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Add a new fruit at the end
fruits.append("Fig")

# Remove the second fruit
fruits.pop(1)

# Print the updated list
print(fruits)




# 6.Write a program to input 3 numbers and print the greatest one.

# Input three numbers
num1 = 25
num2 = 15
num3 = 20
# Determine the greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print(f"The greatest number is: {greatest}")
lowest = min(num1, num2, num3)
print(f"The lowest number is: {lowest}")

 
    
    
# 7. Make a tuple of cities and print each city in a separate line.

cities = ("New York", "London", "Tokyo", "Paris", "Sydney")

for city in cities:
    print(city)


# 8. Take a number from the user and check if it lies between 10 and 20.

# Taking input from the user
number = 25

# Checking if the number lies between 10 and 20
if 10 <= number <= 20:
    print("The number lies between 10 and 20.")
else:
    print("The number does not lie between 10 and 20.")



# 9. Create a set of even numbers between 1 and 10 and remove the number 4.

even_numbers = {2, 4, 6, 8, 10}

# Remove the number 4
even_numbers.remove(4)

print(even_numbers)



# 10. write a dictionary of 3 students with name as key and marks as value.Print students who secored more than 70.
students = {
    "Alice": 85,
    "Bob": 65,
    "Charlie": 72
}
for student, marks in students.items():
     if marks > 70:
         print(f"{student} scored {marks} marks.")


# 11. Create a list of numbers and double each number using list comprehension.
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)




# 12. Ask user to enter a string and check if it is a palindrome.
# Taking input from the user
# user_input = (5, 6, 7, 8, 9, 10)
user_input = "madam"

# Check if the string is a palindrome
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


   
# 13. Input a sentence and count how many times each word appears using a dictionary.

# Input a sentence from the user
sentence = "Hello world! Hello everyone. Welcome to the world of Python programming."

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    word_count[word] = word_count.get(word, 0) + 1

# Print the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")
    
    
    
    
# 14. Create a program that swaps two variables without using a third variable.

a = 5
b = 10

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)




# 15. Input a number and check whether it is a prime number.
num = 5

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")




# 16. Input 5 numbers from the user and store in a list. Then sort them alphabetically.
numbers = []
for _ in range(5):
    num = input("Enter a number: ")
    numbers.append(num)

numbers.sort()
print("Sorted numbers alphabetically:", numbers)





# 17. Create a dictionary from two lists, one of keys and one of values.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Creating the dictionary
dictionary = dict(zip(keys, values))

print(dictionary)



# 18. Find the sum of only even numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example list
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)


# 19. Write a program that counts vowels in a string.

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage
string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(string)}")





# 20. Create a set with duplicate elements and show how duplicates are removed.
# Create a set with duplicate elements
duplicate_set = {1, 2, 2, 3, 4, 4, 5}

# Print the set to show duplicates are removed
print("Set with duplicates removed:", duplicate_set)



# 21. Make a program to check if a year is leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    

# 22. Create a program that counts how many positive and negative numbers are in a list.
numbers = [10, -5, 3, -2, 0, 7, -8, 15]
positive_count = 0
negative_count = 0

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Positive numbers count:", positive_count)
print("Negative numbers count:", negative_count)




# 23. Input a sentence and print all words with length more than 4.
sentence = input("Enter a sentence: ")
words = sentence.split()
long_words = [word for word in words if len(word) > 4]
print("Words with length more than 4:", long_words)



# 24. Create a list and remove all odd numbers from it.

# Example list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Remove odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("List after removing odd numbers:", even_numbers)





# 25. Use a dictionary to count the number of characters in a string.

def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage
string = "hello world"
result = count_characters(string)
print(result)






# 26. Write a program to reverse tuple.
# Define a tuple
original_tuple = (1, 2, 3, 4, 5)

# Reverse the tuple
reversed_tuple = original_tuple[::-1]

# Print the reversed tuple
print("Original Tuple:", original_tuple)
print("Reversed Tuple:", reversed_tuple)





# 27. Check if an item exists in a set.
my_set = {1, 2, 3, 4, 5}
item_to_check = 3

if item_to_check in my_set:
    print(f"{item_to_check} exists in the set.")
else:
    print(f"{item_to_check} does not exist in the set.")




# 28. Create a program to display multiplication table of a number.
number = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
    
    
    

# 29. Ask the user to enter 5 numbers and store only unique numbers in a set.
unique_numbers = set()
for _ in range(5):
    num = int(input("Enter a number: "))
    unique_numbers.add(num)

print("Unique numbers:", unique_numbers)



# 30. Create a menu driven calculator using if-else.
def calculator():
    print("Menu Driven Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"Result: {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please select a valid option.")

calculator()