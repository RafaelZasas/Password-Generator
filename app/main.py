"""
Main file which will be ran by docker
"""
from fastapi import FastAPI, Header
from typing import Optional
import sys
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

sys.path.insert(0, '../../src')
sys.path.append('../../src')

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200/",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


@app.get("/", summary="Home dir")
async def root():
    """
    Function to return data on home dir
    """
    return {"message": "Hello User"}


@app.get("/password", summary="Get a randomly generated password")
async def read_item(pwd_length: Optional[int] = 5,
                    use_symbols: Optional[bool] = True,
                    use_numbers: Optional[bool] = True,
                    use_letters: Optional[bool] = True,
                    strange_header: str = Header(None)) -> JSONResponse:
    """
    Requires Params:<br>
    - pwd_length: (int) Length of password to be generated.
    - use_symbols: (bool) Whether or not to use symbols in pwd generation
    - use_symbols: (bool) Whether or not to use symbols in pwd generation
    - use_symbols: (bool) Whether or not to use symbols in pwd generation

    Returns:<br>
    - randomly generated password

    """

    from app.PasswordGenerator import pwdg
    pwd = pwdg.PasswordGenerator().generate_password(p_length=pwd_length, use_symbols=use_symbols, use_numbers=use_numbers, use_letters=use_letters)
    response = {"password": pwd}
    return JSONResponse(response)
