install:
	poetry install
runserver:
	poetry run mysite/manage.py runserver
lint:
	poetry run flake8 page_analyzer
makemigrations:
	poetry run manage.py makemigrations
migrate:
	poetry run manage.py migrate
gunicorn:
	python -m gunicorn mysite.asgi:application -k uvicorn.workers.UvicornWorker
