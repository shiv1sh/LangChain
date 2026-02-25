from pydantic import BaseModel
from typing import Optional

class user(BaseModel):
    name: str = 'Shivansh' # Setting a default value for the 'name' field
    age : Optional[int] = None # Setting a default value for the 'age' field

user1 = {}

student1 = user(**user1)

print(student1)