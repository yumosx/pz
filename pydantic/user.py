from pydantic import BaseModel, Field
from pydantic.v1 import EmailStr


class User(BaseModel):
    name: str = Field(examples=["Arjain"])
    email: EmailStr = Field(examples=["@example@arjancodes.com"])