## remove all build, test, coverage and Python artifacts
clean: clean-build clean-pyc clean-test

## remove build artifacts
clean-build:
	@echo CLEANING
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

## remove Python file artifacts
clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

## remove test and coverage artifacts
clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

# format the code using black
format:
	@echo FORMATTING
	@black app/

# lint the code using pylint and flake8
lint:
	@echo LINTING
	@python3 -m flake8 app/
	@python3 -m pylint app/

# run the tests using pytest
test:
	@echo TESTING
	@python3 -m pytest -vv --cov=. --cov-report=html

# run all tests and then lint the code
tests: test clean lint

# deploying the code
deploy: tests format lint	

# run the code
run:
	@echo RUNNING
	@python3 app/run.py
