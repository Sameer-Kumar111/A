

# Loop Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


# join sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps only the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.


# union
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # {'a', 'b', 'c', 1, 2, 3}




# you can use the | operator  instead of the union() method, and you will get the same result:
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  # {'a', 'b', 'c', 1, 2, 3}




# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Peter", "Vicky"}
set4 = {"apple", "banana", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)  # {'a', 'b', 'c', 1, 2, 3, 'John', 'Peter', 'Vicky', 'apple', 'banana', 'cherry'}






# When using the | operator, separate the sets with more | operators:
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Peter", "Vicky"}
set4 = {"apple", "banana", "cherry"}
myset = set1 | set2 | set3 | set4
print(myset)  # {'a', 'b', 'c', 1, 2, 3, 'John', 'Peter', 'Vicky', 'apple', 'banana', 'cherry'}





# Join a Set and a Tuple

x = {"apple", "banana", "cherry"}
y = (1, 2, 3)
z = x.union(y)
print(z)  # {1, 2, 3, 'banana', 'cherry', 'apple'}



# update

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)  # {'a', 'b', 'c', 1, 2, 3}


# Intersection 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)  # {'apple'}