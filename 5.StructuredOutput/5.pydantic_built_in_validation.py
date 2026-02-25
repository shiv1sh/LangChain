from pydantic import BaseModel, EmailStr, Field
class user(BaseModel):
    name: str = 'Shivansh'
    email: EmailStr
    cgpa : float = Field(gt=0.0, lt=10.0, description = 'CGPA must be between 0.0 and 10.0', default = 5) # Setting a default value for the 'name' field

new_user = { 'email': 'abc' }
student = user(**new_user)


# converiosn to dictionary
student_dict = dict(student)
print(student_dict['cgpa'])

# converiosn to json
student_json = student.model_dump_json()
print(student_json)

## In this code, we have defined a Pydantic model called `user` with two fields: `name` and `email`. The `name` field has a default value of 'Shivansh', while the `email` field is of type `EmailStr`, which means it expects a valid email address.
print(student)

