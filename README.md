# Password Manager 🗃

[![Stars](https://img.shields.io/github/stars/RafaelZasas/Password-Generator.svg)](https://github.com/RafaelZasas/Raff-App.git/stargazers)
[![Forks](https://img.shields.io/github/forks/RafaelZasas/Password-Generator.svg)](https://github.com/RafaelZasas/Raff-App.git/network/members)
[![Build](https://github.com/RafaelZasas/Password-Generator/workflows/Password%20Generator/badge.svg)](https://github.com/RafaelZasas/Raff-App.git/)


[![Issues](https://img.shields.io/github/issues/RafaelZasas/Raff-App.svg)](https://github.com/RafaelZasas/Raff-App.git/issues)
[![License](https://img.shields.io/github/license/RafaelZasas/Raff-App.svg)](https://opensource.org/licenses/MIT)
## What is this all about? 💬
This is a small scale OSS project for `newbs` like me to practice
with and make something that might look cool on a resume 📝.<br>



## What you need to know:
- This app is written in Python 3.8. 
- Main purpose of this program \[currently\] is to act as a
 web integrated and mobile, random password generator. (Just for fun why not? 🙈)
 An example can be found on my [website]
 
- I've chosen to use [`FastApi`](https://fastapi.tiangolo.com/) as our API framework
  for the backend python functionality. but at some point Id like to make a [GraphQl](https://graphql.org/) version too. (Maybe someone can commit? 👥)

- ***<span style="color:red; ">Important 💥</span>***
Please see the [`CONTRIBUTING.md`](docs/CONTRIBUTING.md)
guidelines before pushing to any branches on this repo.

### Usage:
- see [`FastApi`](https://fastapi.tiangolo.com/) for in depth 
api details.
- Ensure you have a *local virtual environment* setup and 
`pip install requirements`.
- navigate to the **src** folder and run the following command:
    - `uvicorn main:app --reload`
- This will start a locally hosted server at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
- you can then make requests to the api by specifying a url with 
parameters if need be.
- To see what requests can be made navigate to the `/docs` page
where you will be greeted with the beautiful **swaggerUI**.


### References:

- [FastApi](https://fastapi.tiangolo.com/)
- [The Django Project](https://www.djangoproject.com/) 
- [Swagger UI](https://github.com/swagger-api/swagger-ui)
- [Contributing guidelines](docs/CONTRIBUTING.md)
- [Security](docs/CONTRIBUTING.md)
- [License](docs/CONTRIBUTING.md)


