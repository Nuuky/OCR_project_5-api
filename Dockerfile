FROM python:3.10

RUN apt update & apt install

WORKDIR /home/app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-root

COPY server.py .
COPY api/ ./api/

CMD ["python", "server.py"]