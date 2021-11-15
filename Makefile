install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest tests
package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl
build-reinstall:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl