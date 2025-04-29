# Set(Unique values store karte hai)
unique_numbers = {1, 2, 3, 1, 2}
print(unique_numbers)




# Duplicates Not Allowed
thisset = {"grapes", "cherry", "banana", "apple", "apple"}
print(thisset)


thisset = {"apple", "banana", "cherry",  True, 1, 2, 3}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3}
set3 = {True, False, False}
set4 = {1.1, 2.2, 3.3}
set5 = {1, "apple", 1.1, True}
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)


# type()
set1 = {"apple", "banana", "cherry"}
print(type(set1))
set2 = {1, 2, 3}
print(type(set2))
set3 = {True, False, False}
print(type(set3))
set4 = {1.1, 2.2, 3.3}
print(type(set4))
set5 = {1, "apple", 1.1, True}
print(type(set5))




# The set() Constructor
thisset = set(("apple", "banana", "cherry"))
print(thisset)
thisset = set((1, 2, 3))
print(thisset)
thisset = set((True, False, False))
print(thisset)


# Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
    
    







# Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)



# check if "banana" is NOT present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)




# Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"mango", "pineapple", "papaya"}
thisset.update(tropical)
print(thisset)



# Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)



# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)




# discard() method removes the specified item from the set.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)



# pop() method removes the last item from the set.
# banana ko pop karne ko hi hai
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)  # banana ko pop karega
print(thisset)








# clear() method empties the set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) 




# The del keyword will delete the set completely.
thisset = {"apple", "banana", "cherry"}
print("Pehle:", thisset)

del thisset  # Set delete ho gaya

# Ab try karo usko print karne ka (error handle karke)
try:
    print("Baad mein:", thisset)
except NameError:
    print("Set delete ho chuka hai, variable exist nahi karta.")




# the del keyword will delete the set completely.

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)  # NameError: name 'thisset' is not defined

