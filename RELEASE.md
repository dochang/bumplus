# Commands

```sh
pipx run pipenv run python setup.py clean
pipx run pipenv run python setup.py sdist bdist_wheel --universal
pipx run pipenv run twine upload dist/*
# For testpypi
# pipx run pipenv run twine upload --repository testpypi dist/*
```
