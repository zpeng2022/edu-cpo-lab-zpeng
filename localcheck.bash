#coverage report *.py
pycodestyle .
pyflakes .
mdl README.md
# mypy . --strict
coverage run -m pytest --verbose
