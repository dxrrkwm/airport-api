FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN adduser \
    --disabled-password \
    --gecos "" \
    --no-create-home \
    appuser

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

EXPOSE 8000

CMD python manage.py runserver
