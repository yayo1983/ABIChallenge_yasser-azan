from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float
    
class ItemDefault(BaseModel):
    pass

class ItemResponse(BaseModel):
    message: str
    type: str
