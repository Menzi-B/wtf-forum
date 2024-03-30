#!usr/bin/env bash

echo "Building projects packages..."
python3 -m pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "collecting static files..."
python3 manage.py collectstatic --noinput
