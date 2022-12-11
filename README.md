# Groundhog

![Dev workflow](https://github.com/jbettenh/groundhog/actions/workflows/dev_build.yml/badge.svg)
![PROD workflow](https://github.com/jbettenh/groundhog/actions/workflows/prod_pipeline.yml/badge.svg)
[![codecov](https://codecov.io/github/jbettenh/groundhog/branch/trunk/graph/badge.svg?token=F6F4DKBV5C)](https://codecov.io/github/jbettenh/groundhog)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## CS50 Final Project

### Week 10 Documentation

Created by: Joseph Bettenhausen

[Week 10 Specification](https://cs50.harvard.edu/x/2022/project/)

#### Video Demo:

#### Description:

This is a Flask application for the final project of CS50. The title of the project is called `Groundhog`. This app allows users to record any sighting of a groundhog they have seen.

## Project Structure:

The project structure is shown below. Flask is very flexible and doesn't standardize the layout. I have chosen to use the application factory pattern.

```bash
groundhog
|-- .github
|   |-- workflows
|       |-- codecov.yml
|       |-- dev_build.yml
|       `-- prod_pipeline.yml
|-- .venv
|-- groundhog
|   |-- __init__.py
|   |-- auth.py
|   |-- chances.py
|   |-- helpers.py
|   |-- models.py
|   |-- routes.py
|   |-- static
|   |   `-- styles.css
|   `-- templates
|       |-- about.html
|       |-- auth
|       |   |-- login.html
|       |   `-- register.html
|       |-- base.html
|       |-- history.html
|       |-- index.html
|       |-- map.html
|       |-- sighting.html
|       `-- zoo.html
|-- .env
|-- .env.template
|-- .gitignore
|-- config.py
|-- LICENSE
|-- poetry.lock
|-- pyproject.toml
|-- README.md
|-- requirements.txt
`-- tests
    |-- conftest.py
    |-- functional
    |   |-- __init__.py
    |   |-- test_auth.py
    |   `-- test_routes.py
    |-- test.db
    `-- unit
        |-- __init__.py
        |-- test_chances.py
        |-- test_config.py
        |-- test_helpers.py
        |-- test_models.py
        `-- test_templates.py
```

### Environment and depencdency management

I chose to use Poetry for environment and dependency management.

- .venv

### groundhog - Project root

The following files exist in the project root directory.

- .env
- .env.template
- .gitignore
- config.py
- LICENSE
- poetry.lock
- pyproject.toml
- README.md
- requirements.txt

The `.env` file contains secrets like passwords and API keys and should not be uploaded to public repositories! I have included a sample as `.env.template` as a way for people to get started quickly. They just need to add their specific information and remove `.template` from the file name. You can select your configuration via the environment by setting the config class in `CONFIG_TYPE` in .env and the class from `config.py`. The `config.py` shouldn't contain secrets either, so we can upload it to public repositories. This file allows you to have default configurations and build upon that via classes.

The `.gitignore` is needed for projects tracked with Git. This file allows you to not upload temporary files, secrets, or caches that are in the project folder to the public repository.

The `config.py` file contains classes for creating configurations for different environments.

The `LICENSE` file is created from the GitHub template for MIT licenses.

The `poetry.lock` `pyproject.toml` files are created by Poetry.

This `README.md` file is the current file. These are a common way to give information on the project.

The `requirements.txt` file are often still needed for builds such as GitHub Actions CI/CD or SAAS, such as Heroku or Render. Therefore Poetry allows for creating a `requirements.txt` file from the `poetry.lock`.

To create this file, you can the run command:

```
poetry export --with dev --without-hashes --format=requirements.txt > requirements.txt
```

### .github - GitHub Actions Workflows

In the directory .github\workflows contains YAML files for running GitHub actions. The current status includes a build of the project and executing the tests. The `codecov.yml` file is used for configuring non-defaults for the Codecov project. The `dev_build.yml` runs the CI on any commit to any branch other than the trunk branch. The `prod_pipeline.yml` runs the CI on any commit to the trunk branch. This workflow also creates and uploads a test report to Codecov. This allows for the usage of the Codecov badge at the top of this README.md. In the future this workflow would also include a CD component and deploy the app to a SAAS.

.github\workflows

- codecov.yml
- dev_build.yml
- prod_pipeline.yml

### groundhog - Module

### tests - Pytest Tests

The Flask tutorial in the documentation uses Pytest. Pytest is a very popular framework for testing Python projects not just Flask applications. So I was really interested in using it to write my tests.

A command to run all the tests, create a report as well as show the lines which are not yet covered is:

```
pytest --setup-show --cov=groundhog --cov-report term-missing
```

- conftest.py
- test.db

**functional**

- \_\_init\_\_.py
- test_auth.py
- test_routes.py

**unit**

- \_\_init\_\_.py
- test_chances.py
- test_config.py
- test_helpers.py
- test_models.py
- test_templates.py

The `conftest.py` file contains setup and teardown code for the tests. This is used by Pytest. The `test.db` isn't included in the repository as it is created only for some functional tests.

I grouped the tests into two directories either `functional` or `unit` which was based and level of the test. The unit tests individual functions. The functional tests test what the user is interacting with.

## References:

- [Flask application factory tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/)
- [Github Actions examples](https://github.com/mgrum/flask-example-cicd/blob/main/.github/workflows/README.md)
- [Testing Flask applications](https://testdriven.io/blog/flask-pytest/)
