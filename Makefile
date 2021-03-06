PIP := pip install -r

PROJECT_NAME := hoodid
PYTHON_VERSION := 3.6.7
VENV_NAME := ./venv

run:
	python manage.py runserver

db-up:
	python manage.py makemigrations
	python manage.py migrate

delay:
	celery -A ${PROJECT_NAME} worker -l info

celery:
	celery -A ${PROJECT_NAME} beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

shell:
	python manage.py shell

createsuperuser:
	python manage.py createsuperuser

setenve:
	source ../venv/bin/activate