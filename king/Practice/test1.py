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
for i in range(1, 6):  # Outer loop for numbers 1 to 5
    print(f"Multiplication Table of {i}:")
    for j in range(1, 11):  # Inner loop for multiplication from 1 to 10
        print(f"{i} x {j} = {i * j}")
    print()  # Print a newline for better readability between tables
    















# Dictionaries


# Dictionary Items
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict.items()) 






# Ordered or Unordered
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict) 
print(my_dict["name"]) 
print(my_dict["age"]) 
print(my_dict["city"]) 









# Changeable
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
my_dict["age"] = 31  # Change the age
my_dict["city"] = "Los Angeles"  # Change the city
my_dict["name"] = "Jane"  # Change the name
print(my_dict)
print(my_dict["age"])  # Print the updated age
print(my_dict["city"])  # Print the city
print(my_dict["name"])  # Print the name








# Duplicates Not Allowed
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "name": "Jane"  # Duplicate key, will overwrite the previous value
    ,"age": 31,  # Duplicate key, will overwrite the previous value
    "city": "Los Angeles"  # Duplicate key, will overwrite the previous value
}
print(my_dict)  # Print the dictionary
print(my_dict["name"])  # Print the name (will show "Jane" due to overwrite)
print(my_dict["age"])  # Print the age
print(my_dict["city"])  # Print the city






# Dictionary Length
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(len(my_dict))  # Print the length of the dictionary (number of key-value pairs)
print(my_dict["name"])  # Print the name
print(my_dict["age"])  # Print the age
print(my_dict["city"])  # Print the city




# Dictionary Keys
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict.keys())  # Print the keys of the dictionary
print(my_dict["name"])  # Print the name
print(my_dict["age"])  # Print the age
print(my_dict["city"])  # Print the city






# Dictionary Items - Data Types
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [85, 90, 78],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
print(my_dict)  # Print the dictionary
print(my_dict["name"])  # Print the name
print(my_dict["age"])  # Print the age
print(my_dict["city"])  # Print the city
print(my_dict["is_student"])  # Print the is_student status
print(my_dict["grades"])  # Print the grades list
print(my_dict["address"])  # Print the address dictionary
print(my_dict["address"]["street"])  # Print the street from the address dictionary
print(my_dict["address"]["city"])  # Print the city from the address dictionary






# type()
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [85, 90, 78],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
print(type(my_dict))  # Print the type of the dictionary (should be <class 'dict'>)







# Dictionary Methods
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict.get("name"))  # Print the value associated with the key "name"
print(my_dict.get("age"))  # Print the value associated with the key "age"
print(my_dict.get("city"))  # Print the value associated with the key "city"
print(my_dict.get("country", "USA"))  # Print the value associated with the key "country" (default to "USA" if not found)








# The dict() Constructor
my_dict = dict(name="John", age=30, city="New York")
print(my_dict)  # Print the dictionary created using the dict() constructor
print(my_dict["name"])  # Print the name
print(my_dict["age"])  # Print the age
print(my_dict["city"])  # Print the city









# The dict() Constructor with Tuples
my_dict = dict((("name", "John"), ("age", 30), ("city", "New York")))
print(my_dict)  # Print the dictionary created using the dict() constructor with tuples
print(my_dict["name"])  # Print the name
print(my_dict["age"])  # Print the age
print(my_dict["city"])  # Print the city






# Python Collections (Arrays)
# List
my_list = ["apple", "banana", "cherry"]
print(my_list)  # Print the list
print(my_list[0])  # Print the first element of the list
print(my_list[1])  # Print the second element of the list
print(my_list[2])  # Print the third element of the list







# Tuple
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)  # Print the tuple
print(my_tuple[0])  # Print the first element of the tuple
print(my_tuple[1])  # Print the second element of the tuple
print(my_tuple[2])  # Print the third element of the tuple







# Set
my_set = {"apple", "banana", "cherry"}
print(my_set)  # Print the set
print("apple" in my_set)  # Check if "apple" is in the set
print("orange" in my_set)  # Check if "orange" is in the set
print(len(my_set))  # Print the length of the set (number of unique elements)







# Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the dictionary
print(my_dict["name"])  # Print the value associated with the key "name"
print(my_dict["age"])  # Print the value associated with the key "age"
print(my_dict["city"])  # Print the value associated with the key "city"