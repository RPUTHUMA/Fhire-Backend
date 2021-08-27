pip:
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install -e .
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install pytest pytest-cov black importanize pre-commit

install: pip 
	pre-commit install

run:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini FLASK_APP=mainapp \
	FLASK_DEBUG=1 \
	flask run

gunicorn:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini \
	$(PWD)/bin/mlod gunicorn

db-migrate:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini \
	alembic revision

db-upgrade:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini \
	alembic upgrade head

db-downgrade:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini \
	alembic downgrade -1

db:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini \
	alembic upgrade head

db-init:
	FHIRE_SETTINGS=$(PWD)/configs/local.ini \
	alembic init alembic