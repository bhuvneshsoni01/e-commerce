from pydantic import BaseModel


class ItemBase(BaseModel):
    item_name: str
    seller: str
    category: str


class ItemAdd(ItemBase):
    quantity: int
    class Config:
        orm_mode = True


class Item(ItemAdd):
    id: int
    class Config:
        orm_mode = True

