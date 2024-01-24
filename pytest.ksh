python -m pytest -v

coverage run --omit '/usr/lib/python3/dist-packages/*' -m pytest
coverage report
coverage html
