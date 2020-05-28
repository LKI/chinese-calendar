.PHONY: install
install:
	pipenv sync --dev

.PHONY: fix
fix:
	PYTHONPATH=$$(pwd) python chinese_calendar/scripts/__init__.py
	isort -y
	black -l 120 -t py35 -t py36 -t py37 -t py38 .

.PHONY: test
test:
	flake8
	isort --check -rc
	black --check -l 120 -t py35 -t py36 -t py37 -t py38 .
	$(Make) pytest

.PHONY: pytest
pytest:
	pytest
