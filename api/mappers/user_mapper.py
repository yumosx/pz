from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from pydantic import BaseModel, Field


class User(BaseModel):
    __tablename__ = "users"
