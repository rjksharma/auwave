#!/bin/bash

# Activate your virtual environment
source /path/to/your/virtualenv/bin/activate

# Change to your Django project directory
cd /path/to/your/django/project

# Set environment variables if necessary
export DJANGO_SETTINGS_MODULE="auwave.settings"

# Start Gunicorn with your desired configuration
gunicorn wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 2 \
    --log-level=info