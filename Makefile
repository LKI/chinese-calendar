.PHONY: install
install:
	pipenv sync --dev

.PHONY: fix
fix:
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
