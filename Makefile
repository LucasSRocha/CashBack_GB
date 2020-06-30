runserver:
	python manage.py runserver 0.0.0.0:8000

format:
	black .
	isort -rc --atomic .

runtests:
	pytest

local-setup:
	./initial_setup.sh

docker-setup:
	docker-compose build
	docker-compose run web python manage.py loaddata core/fixtures/preapproved.json

run-docker:
	docker-compose up
