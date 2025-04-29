# update Dictionary


# Adding Items

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['email'] = 'abs@gmail.com'
print(my_dict)




# Removing Items

# pop()

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.pop('age')
print(my_dict)


# popitem()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.popitem()
print(my_dict)



# del()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
del my_dict['age']
print(my_dict)



# clear()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.clear()
print(my_dict)




# Dictionary Methods
# python has a set of built-in methods that you can use to manipulate dictionaries.
# Methods                                               Description
# 1.clear()                                             Removes all the elements from the dictionary
# 2.copy()                                              Returns a shallow copy of the dictionary
# 3.fromkeys()                                         Returns a dictionary with the specified keys and values
# 4.get()                                              Returns the value of the specified key
# 5.items()                                            Returns a list containing a tuple for each key value pair
# 6.keys()                                            Returns a list containing the dictionary's keys
# 7.pop()                                             Removes the element with the specified key
# 8.popitem()                                        Removes the last inserted key-value pair
# 9.setdefault()                                    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# 10.update()                                        Updates the dictionary with the specified key-value pairs
# 11.values()                                        Returns a list of all the values in the dictionary




# 1.clear()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.clear()
print(my_dict)  # Output: {}



# 2.Copy()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict2 = my_dict.copy()
print(my_dict2)
print(my_dict is my_dict2)  # False, because they are different objects
print(my_dict == my_dict2)  # True, because they have the same content






# 3.fromkeys()samjhaao
my_dict = dict.fromkeys(['name', 'age', 'city'], 'unknown')
print(my_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}
print(my_dict['name'])  # Output: unknown
print(my_dict['age'])  # Output: unknown
print(my_dict['city'])  # Output: unknown



# 4.get()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.get('name'))  # Output: John
print(my_dict.get('age'))  # Output: 30
print(my_dict.get('city'))  # Output: New York
print(my_dict.get('email'))  # Output: None, because 'email' key does not exist




# 5.items()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(type(my_dict.items()))  # Output: <class 'dict_items'>
print(list(my_dict.items()))  # Output: [('name', 'John'), ('age', 30), ('city', 'New York')]
print(tuple(my_dict.items()))  # Output: (('name', 'John'), ('age', 30), ('city', 'New York'))
print(set(my_dict.items()))  # Output: {('name', 'John'), ('age', 30), ('city', 'New York')}
print(dict(my_dict.items()))  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])



# 6.keys()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(type(my_dict.keys()))  # Output: <class 'dict_keys'>
print(list(my_dict.keys()))  # Output: ['name', 'age', 'city']
print(tuple(my_dict.keys()))  # Output: ('name', 'age', 'city')
print(set(my_dict.keys()))  # Output: {'name', 'age', 'city'}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])




# 7.pop()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

print(my_dict.pop('name'))  # Output: John
print(my_dict)  # Output: {'age': 30, 'city': 'New York'}
print(my_dict.pop('age'))  # Output: 30
print(my_dict)  # Output: {'city': 'New York'}
print(my_dict.pop('city'))  # Output: New York
print(my_dict)  # Output: {}






# 8.popitem()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.popitem())  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'age': 30}
print(my_dict.popitem())  # Output: ('age', 30)
print(my_dict)  # Output: {'name': 'John'}
print(my_dict.popitem())  # Output: ('name', 'John')
print(my_dict)  # Output: {}





# 9.setdefault()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.setdefault('name', 'unknown')) # Output: John
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.setdefault('age', 'unknown'))  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.setdefault('city', 'unknown'))  # Output: New York
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.setdefault('email', 'unknown'))  # Output: unknown
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'unknown'}
print(my_dict.setdefault('email', 'unknown'))  # Output: unknown
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'unknown'}









# 10.update()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.update({'name': 'Jane', 'age': 25, 'city': 'Los Angeles'})
print(my_dict)  # Output: {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}
print(my_dict.update({'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}))  # Output: None
print(my_dict)  # Output: {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}
print(my_dict.update({'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}))  # Output: None
print(my_dict)  # Output: {'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}
print(my_dict.update({'name': 'Jane', 'age': 25, 'city': 'Los Angeles'}))  # Output: None





# 11.values()
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])
print(type(my_dict.values()))  # Output: <class 'dict_values'>
print(list(my_dict.values()))  # Output: ['John', 30, 'New York']
print(tuple(my_dict.values()))  # Output: ('John', 30, 'New York')
print(set(my_dict.values()))  # Output: {'John', 30, 'New York'}
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])





