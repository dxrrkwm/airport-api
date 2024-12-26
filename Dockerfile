FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

POETRY_NO_INTERACTION=1 \
POETRY_VIRTUALENVS_CREATE=false \
POETRY_CACHE_DIR='/var/cache/pypoetry' \
POETRY_HOME='/usr/local' \
POETRY_VERSION=1.8.5

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

RUN adduser \
    --disabled-password \
    --gecos "" \
    --no-create-home \
    appuser

USER appuser

COPY . .

EXPOSE 8000

CMD python manage.py runserver
