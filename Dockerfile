FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install poetry==1.8.5

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

RUN adduser \
    --disabled-password \
    --gecos "" \
    --no-create-home \
    appuser

COPY . .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD python manage.py runserver
