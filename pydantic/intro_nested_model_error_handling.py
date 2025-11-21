from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    name: str
    is_active: bool = False
    
    # Forbids any extra values added to the class
    model_config = ConfigDict(str_max_length=20, extra='forbid')     

class ChatRoom(BaseModel):
    id: int
    room_name: str
    users: list[User] = []

    
p1 = User(id=1, name='Yaswath Kumar')

p2 = {'id': 2, 'name': 'Mahesh', 'is_active': True}
p2 = User(**p2)

print(p1.model_dump())
print(p2.model_dump())

r1 = ChatRoom(id=1, room_name='New')
r2 = {
    'id': 2,
    'room_name': 'Friends',
    'users': [p1, p2]
}
r2 = ChatRoom(**r2)

print(r1.model_dump())
print(r2.model_dump())

try:
    p3 = User(id=3, name='Tester', friends=[p1, p2])
except ValueError as e:
    print(e)