from fastapi import APIRouter
from app.models.item import Item, ItemDefault
from app.presenters.item_presenter import ItemPresenter


class ItemRouter:
    def __init__(self):
        self.router = APIRouter()
        self.presenter = ItemPresenter()
        self.setup_routes()

    def setup_routes(self):
        self.router.get("/", response_model=ItemDefault)(self.default)
        self.router.get("/items/{item_id}", response_model=Item)(self.read_item)

    def read_item(self, item_id: int):
        return self.presenter.get_item(item_id)
    
    def default(self):
        return self.presenter.default()
        
        
