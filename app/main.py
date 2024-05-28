from fastapi import FastAPI
from app.routes import item_route

app = FastAPI()

app.include_router(item_route.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MVP Pattern"}

