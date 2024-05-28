from fastapi import APIRouter
from app.presenters.item_presenter import ItemPresenter

router = APIRouter()
presenter = ItemPresenter()

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return presenter.get_item(item_id)
