# 1. find factorial of a number without using recursion.
# 2. count digits in a number.
# 3. check if a number is an armstrong number (e.g., 153).
# 4. create a pattern of stars using nested loops (5 rows).
# 5. Sum of digits of a number.
# 6. check if a string contains only alphabets.
# 7. Print fibonacci series up to n terms.
# 8. Reverse a number.
# 9. find second largest number from a list.
# 10. find all prime numbers from 1 to 50.



# 1. find factorial of a number without using recursion.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")

# 2. count digits in a number.
def count_digits(number):
    return len(str(abs(number)))

# Example usage
num = 12345
print(f"The number {num} has {count_digits(num)} digits.")

# 3. check if a number is an armstrong number (e.g., 153).

def is_armstrong_number(num):
    # Convert the number to a string to iterate over digits
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

# Example usage
number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
    
    
# 4. create a pattern of stars using nested loops (5 rows).

for i in range(1, 6):  # Outer loop for rows (1 to 5)
    for j in range(i):  # Inner loop for columns
        print("*", end="")  # Print star without newline
    print()  # Move to the next line after each row
    
    
# 5. Sum of digits of a number.
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))



# 6. check if a string contains only alphabets.
string = input("Enter a string: ")

if string.isalpha():
    print("The string contains only alphabets.")
else:
    print("The string contains characters other than alphabets.")
    
    
# 7. Print fibonacci series up to n terms.
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
n_terms = int(input("Enter the number of terms: "))
fibonacci_series(n_terms)




# 8. Reverse a number.
# Input from the user
number = int(input("Enter a number: "))

# Reverse the number
reversed_number = int(str(number)[::-1])

# Output the result
print("Reversed number:", reversed_number)




# 9. find second largest number from a list.
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements to find the second largest
    unique_numbers = list(set(numbers))  # Remove duplicates
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1] if len(unique_numbers) > 1 else None

# Example usage
numbers = [10, 20, 4, 45, 99, 99, 20]
second_largest = find_second_largest(numbers)
print("Second largest number is:", second_largest)




# 10. find all prime numbers from 1 to 50.
for num in range(1, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)