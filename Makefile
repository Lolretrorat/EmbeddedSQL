PROJECT_NAME = EmbeddedSQL
PYTHON = python
PIP = pip

.PHONY: makemigrations migrate runserver shell superuser

makemigrations:
	$(PYTHON) manage.py makemigrations

migrate:
	$(PYTHON) manage.py migrate

run:
	$(PYTHON) manage.py runserver

shell:
	$(PYTHON) manage.py shell

superuser:
	$(PYTHON) manage.py createsuperuser

clean:
	rm -rf $(PROJECT_NAME)/__pycache__ #good lord be careful


