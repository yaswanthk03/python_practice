from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def validate_name(cls, name: str):
        if len(name) < 4:
            raise ValueError("Username must be of at least 4 characters.")
        return name.title()
    
class Password(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def validating_password(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords doesn't match.")
        return self
    
try:
    user1 = User(name='yaswanth kumar')
    print(user1.model_dump())
except ValueError as e:
    print(e)

try:
    password1 = Password(username='yaswanth kumar', password='12345678', confirm_password='12345678')
    print(password1.model_dump())
except ValueError as e:
    print(e)