# FROM python:3.8-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PORT 8080
EXPOSE $PORT

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./app /app

# Install pip requirements
COPY ./requirements.txt /app/requirements.txt
COPY ./setup.py /app/setup.py

RUN /usr/local/bin/python -m pip install --upgrade pip

# Install local Password Generator module
RUN pip install .

RUN pip install --no-cache-dir -r /app/requirements.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]
