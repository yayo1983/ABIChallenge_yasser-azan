from fastapi import APIRouter
from app.schemas.item import Item, ItemDefault
from app.presenters.item_presenter import ItemPresenter
from fastapi import Depends
from app.database import get_db
from sqlalchemy.orm import Session

class ItemRouter:
    def __init__(self):
        self.router = APIRouter()
        self.presenter = ItemPresenter()
        self.setup_routes()

    def setup_routes(self):
        self.router.get("/", response_model=ItemDefault)(self.default)
        self.router.get("/loaddata/", response_model=Item)(self.load_data)
        self.router.get("/unique_variables/", response_model=Item)(self.unique_variables)
        self.router.get("/count_by_product/", response_model=Item)(self.count_by_product) 
        self.router.get("/interpreting_data/", response_model=Item)(self.interpreting_data) 
        

    def default(self):
        return self.presenter.default()
    
    def load_data(self,  db: Session = Depends(get_db)):
        return self.presenter.load_data(db)
    
    def unique_variables(self,  db: Session = Depends(get_db)):
        return self.presenter.unique_variables(db)
    
    def count_by_product(self,  db: Session = Depends(get_db)):
        return self.presenter.count_by_product(db)
    
    def interpreting_data(self,  db: Session = Depends(get_db)):
        return self.presenter.interpreting_data(db)
