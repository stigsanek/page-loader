install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 page_loader tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml
