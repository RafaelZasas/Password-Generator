from fastapi import FastAPI
from pydantic import BaseModel
import sys
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, '/src')
sys.path.append('/src')

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
async def read_item(pwd_length: int = 5, use_symbols: bool = True):
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

