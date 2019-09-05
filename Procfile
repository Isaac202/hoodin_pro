web: gunicorn leggacy.wsgi --log-file -
worker: celery -A leggacy worker -l info
beat: celery -A leggacy beat -l info --scheduler django_celery_beat.