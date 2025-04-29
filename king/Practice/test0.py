# Python - Access Dictionary Items
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict["name"])  # Accessing the value using the key
print(my_dict["age"])  # Accessing the value using the key
print(my_dict["city"])  # Accessing the value using the key









# get()
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict.get("name"))  # Accessing the value using the key
print(my_dict.get("age"))  # Accessing the value using the key
print(my_dict.get("city"))  # Accessing the value using the key






# Get Keys
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict.keys())  # Accessing the keys of the dictionary







# Python - Change Dictionary
my_dict = {
     "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
my_dict["age"] = 31  # Change the age
print(my_dict)  # Print the updated dictionary








# Update Dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
my_dict.update({"age": 31})  # Update the age
print(my_dict)  # Print the updated dictionary
my_dict.update({"city": "Los Angeles"})  # Update the city
print(my_dict)  # Print the updated dictionary






# Python - Add Dictionary Items
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
my_dict["country"] = "USA"  # Add a new key-value pair
print(my_dict)  # Print the updated dictionary








# Python - Remove Dictionary Items

# Remove Dictionary Items


# pop()
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
my_dict.pop("age")  # Remove the key "age"
print(my_dict)  # Print the updated dictionary







# popitem()
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
my_dict.popitem()  # Remove the last inserted key-value pair
print(my_dict)  # Print the updated dictionary








# del
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
del my_dict["age"]  # Remove the key "age"
print(my_dict)  # Print the updated dictionary






# clear()
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
my_dict.clear()  # Clear the dictionary
print(my_dict)  # Print the cleared dictionary









# Python - Loop Dictionary Items
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Print the original dictionary
for key, value in my_dict.items():
    print(key, ":", value)  # Print each key-value pair
        
    

