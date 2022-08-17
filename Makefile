run:
	python manage.py runserver

migrate:
	python manage.py migrate
	python manage.py loaddata fixtures.json