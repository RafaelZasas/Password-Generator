from fastapi import FastAPI
from pydantic import BaseModel
import sys, os

sys.path.insert(0, '/src')
sys.path.append('/src')

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


@app.get("/password", summary="Get a randomly generated password")
async def read_item(pwd_length: int, use_symbols: bool):
    """
    Requires Params:<br>
    - pwd_length: (int) Length of password to be generated.
    - use_symbols: (bool) Whether or not to use symbols in pwd generation

    Returns:<br>
    - randomly generated password

    """

    from PasswordGenerator import pwdg
    pwd = pwdg.PasswordGenerator().generate_password(p_length=pwd_length, use_symbols=use_symbols)
    return {"password": pwd}
