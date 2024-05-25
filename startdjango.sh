#!/bin/sh
cd /home/pi/django
pipenv shell
python manage.py runserver 0.0.0.0:8000