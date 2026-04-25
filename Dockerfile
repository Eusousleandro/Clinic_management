FROM python:3.11-slim as builder

RUN pip install poetry
WORKDIR /app

COPY pyproject.toml poetry.lock* /app/
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]