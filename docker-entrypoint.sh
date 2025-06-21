#!/bin/sh
set -e

PROJECT_NAME="journalpal"

if [ "$1" = "webserver" ]; then

	uv run python manage.py migrate
	uv run python manage.py collectstatic --no-input --clear

	exec uv run gunicorn --workers=2 --bind=0.0.0.0:8000 ${PROJECT_NAME}.wsgi
elif [ "$1" = "celery-worker" ]; then
    exec uv run celery -A ${PROJECT_NAME} worker --concurrency 2 --loglevel=info
elif [ "$1" = "celery-beat" ]; then
    exec uv run celery -A ${PROJECT_NAME} beat --loglevel=info
elif [ "$1" = "djshell" ]; then
    exec uv run python manage.py shell_plus
else
    echo "Unknown command: $1"
    exit 1
fi
