from pydantic import BaseModel, field_validator, Field
from datetime import datetime

class Comment(BaseModel):
    id: int
    content: str
    replies: list['Comment'] = Field(default_factory=list)
    
    created_at: datetime = datetime.now()

    @field_validator('created_at', mode='before')
    def parse_time(cls, value):
        if isinstance(value, str):
            return datetime.strptime(value, '%d-%m-%Y %H-%M-%S')
        return value
    
Comment.model_rebuild()

comment1 = Comment(id=1, content='First comment')
comment2 = Comment(id=2, content='Nice work.', created_at=datetime(2025, 11, 21, 12))

comment3 = {
    'id': 3,
    'content': "Stating a comment reply section.",
    'replies': [
        comment1,
        Comment(id=2, content='Nice work.', created_at=datetime(2025, 11, 21, 12)),
        Comment(id=4, content='new comment section.', 
                replies=[
                    Comment(id=5, content='Last comment')
                ],
                created_at=datetime(2025, 11, 21, 12))
    ]
}

comment3 = Comment(**comment3)

print(comment1.model_dump())
print(comment2.model_dump())
print(comment3.model_dump_json(indent=2))
