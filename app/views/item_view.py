from fastapi.responses import JSONResponse

class ItemView:
    @staticmethod
    def display_item(item):
        item_dict = item.dict()
        return JSONResponse(content=item_dict)
