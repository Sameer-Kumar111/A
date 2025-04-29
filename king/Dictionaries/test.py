# 3. user se 5 number input lo aur uska multiplication table print karo using nested loop. 



# User se 5 numbers input lena
numbers = []
for i in range(5):
    num = int(input(f"Number {i+1} dijiye: "))
    numbers.append(num)

# Har number ke liye multiplication table print karna
for num in numbers:
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
