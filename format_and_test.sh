black --target-version py38 *.py
flake8 --extend-ignore=E203,E501 *.py
python -m pytest test.py
