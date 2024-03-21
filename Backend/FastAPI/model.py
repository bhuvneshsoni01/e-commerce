from sqlalchemy import Boolean, Column, Integer, String
from db_handler import Base


class Items(Base):
    """
    This is a model class. which is having the movie table structure with all the constraint
    """
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    item_name = Column(String(63), index=True, nullable=False)
    seller = Column(String(63), index=True, nullable=False)
    category = Column(String(63), index=True, nullable=False)
    quantity = Column(Integer, index=True, default= 0)