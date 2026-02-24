from typing import TypedDict

class dictSchema(TypedDict):
    name: str
    age: int
    city: str

# this will give us an error if we try to assign a value of wrong type to any of the keys in the dictionary
# also if we assign a string to the int key 'age' it will not give us a error
newDict: dictSchema = {'name' : 'Shivansh', 'age' : 20, 'city' : 'Delhi'}

print(newDict)