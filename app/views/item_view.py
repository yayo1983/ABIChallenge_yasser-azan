from fastapi.responses import JSONResponse

class ItemView:
    @staticmethod
    def display_item(item):
        return JSONResponse(content=item)
