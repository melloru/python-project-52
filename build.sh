#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
poetry install

# Convert static asset files
python mysite/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python mysite/manage.py migrate