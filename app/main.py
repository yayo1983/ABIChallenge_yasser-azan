from fastapi import FastAPI
from app.routes.item_route import ItemRouter

app = FastAPI()

class MainApp:
    def __init__(self, app):
        self.app = app
        self.setup_routes()

    def setup_routes(self):
        item_router = ItemRouter()
        self.app.include_router(item_router.router)

MainApp(app)


