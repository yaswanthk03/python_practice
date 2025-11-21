from pydantic import BaseModel, ConfigDict, PlainSerializer, field_serializer, model_serializer
from typing import List, Annotated
from datetime import datetime

Title_Mode = Annotated[str, PlainSerializer(lambda x: x.title())]

class Address(BaseModel):
    street: Title_Mode
    city: Title_Mode
    zip_code: str

    @field_serializer('zip_code', mode='plain')
    def capitalize_(self, value: str) -> str:
        return value.upper()

class User(BaseModel):
    id: int
    name: Title_Mode
    email: Annotated[str, PlainSerializer(lambda x: x.lower())]
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

class UserModel(BaseModel):
    username: str
    name: str

    @model_serializer(mode='plain')  
    def serialize_model(self) -> str:  
        return f'{self.username} - {self.name}'

print(UserModel(username='yk03', name='Yaswanth Kumar').model_dump())

user = User(
    id=1,
    name="Yaswanth",
    email="YK03@gmail.com",
    createdAt=datetime(2025, 11, 21, 14, 30,),
    address=Address(
        street="SomeThing",
        city="bengaluru",
        zip_code="600001"
    ),
    is_active=False,
)

python_dict = user.model_dump()
print('*' * 50)
print(python_dict)

json_str = user.model_dump_json(indent=2)
print('*' * 50)
print(json_str)