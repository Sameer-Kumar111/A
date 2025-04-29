# ordered or unordered
thisdict = { "brand": "Ford",
             "model": "Mustang",
             "year": 1964,
             "electric": False,
             "colors": ["red", "white", "blue"],}


# duplicate Not allowed
thisdict = { "brand": "Ford",
                "model": "Mustang",
                "year": 1964,
                "electric": False,
                "colors": ["red", "white", "blue"],
                "brand": "BMW"}
print(thisdict)
print(thisdict["brand"])
print(thisdict["brand"])

