FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry uvicorn fastapi sqlalchemy dotenv

COPY pyproject.toml poetry.lock* ./
COPY . .  

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
