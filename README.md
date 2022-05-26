# cookiecutter-tf-module

Cookiecutter template to manage consistent creation of Terraform modules.

## To use this template

```bash
$ pip install cookiecutter GitPython hub python-terraform
$ cookiecutter https://github.com/cookiecutter-tfmodule.git
```

You will be prompted for basic info (your name, module name, etc.) which will be used in the template.

That's all you need to get started.

## Testing the module

The `tests` folder implements a simple test harness.

In order to use the testing suite you will need to do the following:

1. Write test cases that use the module, placing each test case in its own directory under `tests/`, e.g. `tests/<test_case1>`
2. Install `go`
3. Run `make terratest/install` to install the prerequisites
4. Run `make test` for your suite of tests to run

### Example test case
For the most part, you will create simple terraform code that will just instantiate your module
```terraform
module "example_1" {
  source = "../../"

  variable_1 = "alpha"
  variable_2 = "beta"
}
```

Additional test cases will typically alter the variables passed to the module to address other scenarios
```terraform
module "example_2" {
  source = "../../"

  variable_1 = "alpha"
  variable_2 = "gamma"
}
```



## Inputs

You will be asked for these fields:

| Template Variable  | Default | Description |
| ------------------ | ------- | ----------- |
| ``module_name`` | ``template`` | The name of the terraform module that you are creating. |
| ``short_description`` | ``A Terraform Module`` | Description of the terraform module. |
