# Python For Loops ke full methods
#
# 1. for loop with range()
# 2. for loop with list
# 3. for loop with tuple
# 4. for loop with string
# 5. for loop with dictionary
# 6. for loop with set
# 7. for loop with enumerate()
# 8. for loop with zip()
# 9. for loop with filter()
# 10. for loop with map()
# 11. for loop with lambda function
# 12. for loop with list comprehension
# 13. for loop with dictionary comprehension
# 14. for loop with set comprehension
# 15. for loop with generator expression
# 16. for loop with itertools
# 17. for loop with itertools.count()
# 18. for loop with itertools.cycle()
# 19. for loop with itertools.repeat()
# 20. for loop with itertools.chain()
# 21. for loop with itertools.combinations()
# 22. for loop with itertools.permutations()
# 23. for loop with itertools.product()
# 24. for loop with itertools.groupby()
# 25. for loop with itertools.groupby() with key function
# 26. for loop with itertools.groupby() with key function and lambda expression
# 27. for loop with itertools.groupby() with key function and lambda expression and list comprehension
# 28. for loop with itertools.groupby() with key function and lambda expression and dictionary comprehension
# 29. for loop with itertools.groupby() with key function and lambda expression and set comprehension
# 30. for loop with itertools.groupby() with key function and lambda expression and generator expression
# 31. for loop with itertools.groupby() with key function and lambda expression and itertools
# 32. for loop with itertools.groupby() with key function and lambda expression and itertools.count()
# 33. for loop with itertools.groupby() with key function and lambda expression and itertools.cycle()
# 34. for loop with itertools.groupby() with key function and lambda expression and itertools.repeat()
# 35. for loop with itertools.groupby() with key function and lambda expression and itertools.chain()
# 36. for loop with itertools.groupby() with key function and lambda expression and itertools.combinations()
# 37. for loop with itertools.groupby() with key function and lambda expression and itertools.permutations()
# 38. for loop with itertools.groupby() with key function and lambda expression and itertools.product()
# 39. for loop with itertools.groupby() with key function and lambda expression and itertools.groupby()
# 40. for loop with itertools.groupby() with key function and lambda expression and itertools.groupby() with key function
# 41. for loop with itertools.groupby() with key function and lambda expression and itertools.groupby() with key function and lambda expression
# 42. for loop with itertools.groupby() with key function and lambda expression and itertools.groupby() with key function and lambda expression and list comprehension





# 1. for loop with range()

for i in range(5):
    print(i)  # Output: 0 1 2 3 4



# 2. for loop with list
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)  # Output: 1 2 3 4 5
    




# 3. for loop with tuple
my_tuple = (1, 2, 3, 4, 5)
for i in my_tuple:
    print(i)  # Output: 1 2 3 4 5





# 4. for loop with string
my_string = "Hello"
for i in my_string:
    print(i)  # Output: H e l l o
    
    

# 5. for loop with dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in my_dict.items():
    print(key, value)  # Output: name John age 30 city New York





# 6. for loop with set
my_set = {1, 2, 3, 4, 5}
for i in my_set:
    print(i)  # Output: 1 2 3 4 5 (order may vary)
    
    
    
    
# 7. for loop with enumerate()
my_enum = ['a', 'b', 'c', 'd']
for index, value in enumerate(my_enum):
    print(index, value)  # Output: 0 a 1 b 2 c 3 d



# 8. for loop with zip()
my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']
for i, j in zip(my_list1, my_list2):
    print(i, j)  # Output: 1 a 2 b 3 c
    
    
    
# 9. for loop with filter()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_even = filter(lambda x: x % 2 == 0, my_list)
for i in my_even:
    print(i)  # Output: 2 4 6 8 10
    
    
    
# 10. for loop with map()
my_list = [1, 2, 3, 4, 5]
my_square = map(lambda x: x ** 2, my_list)
for i in my_square:
    print(i)  # Output: 1 4 9 16 25
    
    
    
    
    
# 11. for loop with lambda function
my_list = [1, 2, 3, 4, 5]
my_lambda = lambda x: x ** 2
for i in my_list:
    print(my_lambda(i))  # Output: 1 4 9 16 25





#12. for loop with list comprehension
my_list = [1, 2, 3, 4, 5]
my_square = [x ** 2 for x in my_list]
for i in my_square:
    print(i)  # Output: 1 4 9 16 25
    
    
    
    
    
# 13. for loop with dictionary comprehension
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_square = {key: value ** 2 for key, value in my_dict.items()}
for key, value in my_square.items():
    print(key, value)  # Output: a 1 b 4 c 9
    
    

# 14. for loop with set comprehension
my_set = {1, 2, 3, 4, 5}
my_square = {x ** 2 for x in my_set}
for i in my_square:
    print(i)  # Output: 1 4 9 16 25 (order may vary)
    
    
    
    
# 15. for loop with generator expression
my_list = [1, 2, 3, 4, 5]
my_square = (x ** 2 for x in my_list)
for i in my_square:
    print(i)  # Output: 1 4 9 16 25
    






