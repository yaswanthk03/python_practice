from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee name',
    )
    department: str = 'General'
    salary: float = Field(
        ...,
        ge=0,
        le=10000000
    )

employee1 = Employee(id=1, name='Yaswanth', salary=100000)

print(employee1.model_dump())