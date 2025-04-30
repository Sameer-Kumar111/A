# Arbitary Keyword Arguments, **kwargs
# ,
def my_function(**kid):
    print("His last name is" , kid["lname"])
my_function(fname = "Ram", lname = "Refsnes")






# +
def my_function(**kid):
    print("His last name is" + kid["lname"])
my_function(fname = "Ram", lname = "Refsnes")