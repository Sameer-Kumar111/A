# The while Loop

i = 1
while i <= 6:
    print(i)
    i += 1  # Increment i by 1 each time the loop runs
 
 
 
    
    
# The while Loop with a break statement
i = 1
while i <= 6:
    print(i)
    i += 1  # Increment i by 1 each time the loop runs
    if i == 4:
        break  # Exit the loop when i is equal to 4
 
 
 
 
    
# The while Loop with a continue statement
i = 1
while i <= 6:
    i += 1  # Increment i by 1 each time the loop runs
    if i == 4:
        continue  # Skip the rest of the loop when i is equal to 4
    print(i)  # Print i only if it is not equal to 4


# The while Loop with a else statement
i = 1
while i <= 6:
        print(i)
        i += 1  # Increment i by 1 each time the loop runs
else:
        print("Loop ended")  # This will be printed after the loop ends
        