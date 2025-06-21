FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

ENV PYTHONUNBUFFERED=1

ADD . /app

WORKDIR /app

COPY .env.prod .env

RUN uv sync --frozen --no-dev

RUN ["chmod", "+x", "/app/docker-entrypoint.sh"]

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
