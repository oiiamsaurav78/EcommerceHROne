from pydantic import BaseModel
from typing import List, Optional

class ProductModel(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    size: Optional[str] = None

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderModel(BaseModel):
    user_id: str
    items: List[OrderItem]
