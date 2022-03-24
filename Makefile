.PHONY: install
install:
	pipenv sync --dev

.PHONY: fmt
fmt:
	PYTHONPATH=$$(pwd) python chinese_calendar/scripts/__init__.py
	isort .
	black -l 120 .

.PHONY: test
test:
	flake8
	isort --check .
	black --check -l 120 .
	$(Make) pytest

.PHONY: pytest
pytest:
	pytest


.PHONY: release
release:
	rm -rf dist
	python setup.py release
	twine upload -r pypi dist/*
	sed -i 's/chinesecalendar/chinese_calendar/g' setup.py
	python setup.py release
	twine upload -r pypi dist/*
