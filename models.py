# models.py
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    making_time = Column(String(100), nullable=False)
    serves = Column(String(100), nullable=False)
    ingredients = Column(String(300), nullable=False)
    cost = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
