# Password Manager

![Build](https://github.com/RafaelZasas/Password-Generator/workflows/Python%20application/badge.svg?branch=master)

## What is this all about?
This is a small scale OSS project for `newbs` like me to practice
contributing to something that might look cool on a resume.<br>
I'd like to have an API that can be used within websites 
to display small python backend functions.


## What you need to know:
- This app is written in Python 3.8. 
- Main purpose of this program \[currently\] is to act as a
 web integrated, random password generator.
 
- We've chosen to use [`FastApi`](https://fastapi.tiangolo.com/) as our API framework
  for the backend python functionality.

- ***<span style="color:red; ">Really Important:</span>***
Please see the [`CONTRIBUTING.md`](docs/CONTRIBUTING.md)
guidelines before pushing to any branches on this repo.

### Usage:
- see [`FastApi`](https://fastapi.tiangolo.com/) for in depth 
api details.
- Ensure you have a *local virtual environment* setup and 
`pip install requirements`.
- navigate to the **src** folder and run the following command:
    - `uvicorn main:app --reload`
- This will start a locally hosted server at **http://127.0.0.1:8000/**
- you can then make requests to the api by specifying a url with 
parameters if need be.
- To see what requests can be made navigate to the `/docs` page
where you will be greeted with the beautiful **swaggerUI**.


### Links:

- [FastApi](https://fastapi.tiangolo.com/)
- [The Django Project](https://www.djangoproject.com/) 
- [Swagger UI](https://github.com/swagger-api/swagger-ui)
- [Contributing guidelines](docs/CONTRIBUTING.md)
- [Security](docs/CONTRIBUTING.md)
- [License](docs/CONTRIBUTING.md)


#### Additional info:
- Why not use Django?
    <p>Django is a complicated framework to learn 
    and use in itself, has features
     we don't need and doesn't come 
     with a cool Swagger UI.</p>
