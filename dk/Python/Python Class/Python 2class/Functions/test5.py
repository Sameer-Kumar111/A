# Arbitrary Argument, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Ram", "Kumar", "Shyam", "Hari")






# keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1="Ram", child2="Shyam", child3="Hari")
