from fastapi import FastAPI
from pydantic import BaseModel
import src.PasswordGenerator
app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/", summary="Home dir")
async def root():
    """
    Function to return data on home dir
    """
    return {"message": "Hello User"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/password")
def read_item( q: str = None):
    pg = src.PasswordGenerator.PasswordGenerator()
    pwd = pg.generate_password()
    return {"password": pwd, "q": q}
