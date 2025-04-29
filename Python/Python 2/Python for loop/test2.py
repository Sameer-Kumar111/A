# The break Statement

# With the break statement we can stop the loop before it has looped through all the items:

fruits = ["apple", "banana", "cherry"]
for i in fruits:
  print(i) 
  if i == "banana":
    break