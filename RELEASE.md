# Commands

```sh
pipenv run python setup.py clean
pipenv run python setup.py sdist bdist_wheel --universal
pipenv run twine upload dist/*
# For testpypi
# pipenv run twine upload --repository testpypi dist/*
```
