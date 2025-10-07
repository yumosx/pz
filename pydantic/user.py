from typing import Any, Self

from pydantic import BaseModel, Field, field_validator, model_validator
from pydantic.v1 import EmailStr

VALID_NAME_REGEX = ""

class User(BaseModel):
    name: str = Field(examples=["Arjain"])
    email: EmailStr = Field(examples=["@example@arjancodes.com"])

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not VALID_NAME_REGEX.match(value):
            raise ValueError("")
        return value

    @field_validator("name", mode="before")
    @classmethod
    def validate_name(cls, value:str) -> str:
        # 表示在数据验证之前
        if isinstance(value, str):
            return value.replace(',', '')
        return value

    @model_validator(mode="before")