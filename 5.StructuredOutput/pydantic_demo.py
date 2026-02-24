from pydantic import BaseModel

class user(BaseModel):
    name: str

new_user = { 'name' : 'Shivansh'}

student = user(**new_user)

print(student)


# Good question 👍

# **new_user is dictionary unpacking in Python.

# Your dictionary:

# new_user = { 'name': 'Shivansh' }

# Your Pydantic model expects:

# class user(BaseModel):
#     name: str

# Which means the constructor looks like:

# user(name="Shivansh")

# When you write:

# student = user(**new_user)

# Python converts it to:

# student = user(name='Shivansh')

# So ** takes dictionary keys → turns them into named arguments.

# Without **, this would happen:

# student = user(new_user)   # ❌ Wrong

# Now Python tries to pass the whole dict as a single positional argument, which the model does not expect → error.

# ✅ Rule of thumb:
# 	•	* → unpack list/tuple (positional)
# 	•	** → unpack dict (keyword arguments)

# Example:

# data = {"name": "Shivansh"}
# user(**data)   # same as user(name="Shivansh")

# That’s why we use ** here.