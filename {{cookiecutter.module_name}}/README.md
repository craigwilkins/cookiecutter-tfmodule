# {{cookiecutter.module_name}}

{{cookiecutter.short_description}}


## Testing
Here we've included pytest and pytest-tftest to run basic tests. Examples are included for testing `terraform apply` and `terraform plan`.

I've included a sample provider pointing to localhost for use with localstack.

```
pip install -r ./tests/requirements.txt
pytest .
```

This should lint any python files in the project and run the sample tests.


## pre commit hook installation
We've included a pre-commit hook here, you don't have to use it.

```
pip install pre-commit
pre-commit install
```
