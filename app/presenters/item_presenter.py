from app.models.item import Item
from app.views.item_view import ItemView

class ItemPresenter:
    def get_item(self, item_id: int):
        example_item = Item(id=item_id, name="Item Example", description="This is an example", price=10.0)
        return ItemView.display_item(example_item)
