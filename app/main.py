"""
Main file which will be ran by docker
"""
from fastapi import FastAPI, Header
from typing import Optional
import sys
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


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

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/404")


@app.get("/404", summary="404 - Not Found")
async def root():
    """
        404 - Page Not Found. Non existent entrypoints will redirect here.
    """

    html_content = """
        <html>

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Tailwind CSS -->
        <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
        <title>Password Generator</title>
    </head>

    <body>
        <main class="min-h-full bg-cover bg-top sm:bg-top"
            style="background-image: url('https://images.unsplash.com/photo-1545972154-9bb223aac798?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=3050&q=80&exp=8&con=-15&sat=-75');">
            <div class="max-w-7xl mx-auto px-4 py-16 text-center sm:px-6 sm:py-24 lg:px-8 lg:py-48">
                <p class="text-sm font-semibold text-black text-opacity-50 uppercase tracking-wide">404 error</p>
                <h1 class="mt-2 text-4xl font-extrabold text-white tracking-tight sm:text-5xl">Uh oh! I think you’re lost.
                </h1>
                <p class="mt-2 text-lg font-medium text-black text-opacity-50">
                Welcome to my Random Password API
                </p>
                <div class="mt-6">
                    <a href="docs"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        Go to Interactive Docs
                    </a>
                </div>

                <div class="mt-6">
                    <a href="redoc"
                        class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-black text-opacity-75 bg-white bg-opacity-75 sm:bg-opacity-25 sm:hover:bg-opacity-50">
                        ReDoc
                    </a>
                </div>
            </div>
        </main>
    </body>

    </html>
        """
    return HTMLResponse(content=html_content, status_code=200)


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
    pwd = pwdg.PasswordGenerator().generate_password(p_length=pwd_length, use_symbols=use_symbols,
                                                     use_numbers=use_numbers, use_letters=use_letters)
    response = {"password": pwd}
    return JSONResponse(response)
