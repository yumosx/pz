from pydantic import BaseModel

class Name(BaseModel):
    name: str
    age: int
    phone: str