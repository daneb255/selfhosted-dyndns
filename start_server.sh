#!/bin/bash

cd /opt/dyndns/dyndns-update-script

. $(pipenv --venv)/bin/activate

exec gunicorn --bind 127.0.0.1:5000 --log-level=info --log-file=/var/log/gunicorn.log --worker-class=gthread --pid gunicorn.pid wsgi:app
