web: gunicorn hoodid.wsgi --log-file -
worker: celery -A hoodid worker -l info
beat: celery -A hoodid beat -l info --scheduler django_celery_beat.