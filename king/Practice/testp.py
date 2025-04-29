#The while Loop
i = 1
while i < 6:
  print(i)
  i += 1
    









# The while Loop with a break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
  
  
  
  
  
  
  
  
#   The while Loop with a continue statement
i = 1
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  
  
  
  
  
  
  
  
  
#   The while Loop with a else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  
  
  
  
  
  
  
  
# Multiplication Table (Nested Loops)
for i in range(1, 6): 
    print(f"Multiplication Table of {i}:")
    for j in range(1, 11):  
        print(f"{i} x {j} = {i * j}")
    print()  
    
