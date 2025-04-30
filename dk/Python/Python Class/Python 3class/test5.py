# Positional-Only Arguments

def my_function(x, y, /):
    print(x, y)
my_function(1, 2)





# , /
def my_function(x):
    print(x)
my_function(x = 3)


    
    
    
# , /
def my_function(x, /):
    print(x)
my_function(x = 3)