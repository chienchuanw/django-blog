# Django-related
server:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser

# Project-initialization
gitignore:
	echo ".venv" > .gitignore
	echo ".env" >> .gitignore
	echo "__pycache__" >> .gitignore
	echo "*.sqlite3" >> .gitignore
	echo "node_modules" >> .gitignore
	echo "static/styles/output.css" >> .gitignore
	echo "static/scripts/output.js" >> .gitignore

environ:
	echo "DJANGO_SECRET_KEY=" > core/.env
	echo "DJANGO_SECRET_KEY=your-secret-key" > core/.env.example

readme:
	touch README.md

