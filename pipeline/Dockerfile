
From python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

Workdir /app

ENV PATH="/app/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" "README.md" ./

COPY src/ ./src/
COPY ingest_data.py .

RUN uv sync --locked


Entrypoint ["python", "ingest_data.py"]