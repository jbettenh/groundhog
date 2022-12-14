# Groundhog

![Dev workflow](https://github.com/jbettenh/groundhog/actions/workflows/dev_pipeline.yml/badge.svg)
![PROD workflow](https://github.com/jbettenh/groundhog/actions/workflows/prod_pipeline.yml/badge.svg)
[![codecov](https://codecov.io/github/jbettenh/groundhog/branch/trunk/graph/badge.svg?token=F6F4DKBV5C)](https://codecov.io/github/jbettenh/groundhog)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## CS50x Introduction to Computer Science

### Final Project - Week 10 Documentation

Created by: Joseph Bettenhausen, 2022, Düsseldorf, Germany

[Week 10 Specification](https://cs50.harvard.edu/x/2022/project/)

#### Video Demo:

[Groundhog Demo a Flask App](https://youtu.be/kv86SawKgdg)

#### Description:

This is a Flask application for the final project of CS50X. The title of the project is called `Groundhog`. This app allows users to record sightings of groundhogs within the continental United States.

I chose to use [Poetry](https://pypi.org/project/poetry/) for environment and dependency management. I have experience with Poetry and found it easy to use. It is also becoming very popular among Python developers and I wanted to have more exposure to it.

Even though I have experience creating Django applications, I chose to make a [Flask](https://pypi.org/project/Flask/) application. This would allow me to use my Python knowledge and expand my exposure to Flask, which was introduced in Week 9 of the CS50X course.

I opted not to use the CS50 library for SQL and instead chose to use [Flask SQL Alchemy](https://pypi.org/project/flask-sqlalchemy/). It is an extension for Flask which makes it easier to use SQLAlchemy. SQLAlchemy is an Object Relational Mapper (ORM), which are often used in larger projects to simplify querying and abstract away the specific database systems. As I didn't have a lot of experience with an ORM before, I thought it important to pick one for ease of use, setup, with good documentation, and examples. I wanted to implement SQLAlchemy into the project, because it has received a lot of good reviews for usage with Python.

It is said, that code is more often read than it is written. Therefore formatting and linting are important. That is why I picked the popular packages [Black](https://pypi.org/project/black/) and [Flake8](https://pypi.org/project/flake8/) to format and lint my code. Both were easy to setup and immediately useful in improving the code quality. I was also able to set them up on pre-commit check, so that they are always checking the code on every commit.

The tutorial from the official Flask documentation uses [Pytest](https://pypi.org/project/pytest/). Pytest is a reliable and detailed framework for testing Python projects not just Flask applications. I was really interested in using it to write my tests and to further my experience with it.

## Project Usage

The project focuses on tracking your groundhog sightings.

Since the project uses Flask-Migrate, the following command can be used to update your db to the latest version:

```
flask db upgrade
```

The project comes with 2 Zoos that stated they had groundhogs. To insert them into the database use the CLI command:

```
flask create-zoos
```

To the run the application from the root project directory execute the command:

```
flask run
```

The application consists of a few different pages. The following section gives an overview.

### Homepage

This is the start page for the application and is accessible without logging in.
![Screenshot of homepage with pictures of groundhogs and information about them.](/demo/home.JPG)

### Register

Here the user can create a username, include their email, and create a password.
![Screenshot of register page.](/demo/register.JPG)

### Login

On this page the user can login with created username and password from the registraion page.
![Screenshot of login page.](/demo/login.JPG)

### Map

This page shows all of the sightings from the database using markers.
![Screenshot of a map with markers of sightings of groundhogs.](/demo/map.JPG)

### Zoo

This page shows a list of zoos in the database. As mentioned above a few default zoos can be created with the CLI.
![Screenshot of page with information about zoos with groundhogs.](/demo/zoo.JPG)

### Add Sighting

This page provides a form for the user to add the location about a sighting of a groundhog.
![Screenshot of page to add a new sighting of a groundhog.](/demo/sighting.JPG)

### Tracking History

This page shows the results for all sightings in the database.
![Screenshot of page showing table of documented sightings.](/demo/history.JPG)

## Project Structure:

The project structure is shown below. It includes files, which are not committed to GitHub. They are mentioned here to give a complete picture of the final project. Flask is very flexible and doesn't standardize the layout. I have chosen to use the [application factory pattern](https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/).

```bash
groundhog
|-- .github
|   |-- codecov.yml
|   |-- workflows
|       |-- dev_pipeline.yml
|       `-- prod_pipeline.yml
|-- .venv
|-- groundhog
|   |-- __init__.py
|   |-- auth.py
|   |-- helpers.py
|   |-- models.py
|   |-- routes.py
|   |-- static
|   |   |-- css
|   |   |   |-- main.min.css
|   |   |   |-- main.min.css.map
|   |   |-- images
|   |   |   |-- groundhog_brand.png
|   |   |   |-- groundhog_main.jpeg
|   |   |   |-- groundhog_sighting.jpeg
|   |   |   |-- habitat_leaf.png
|   |   |   `-- seasons.png
|   |   |-- node_modules
|   |   |-- sass
|   |        `-- main.css
|   |   |-- package-lock.json
|   |   |-- package.json
|   `-- templates
|       |-- auth
|       |   |-- login.html
|       |   `-- register.html
|       |-- base.html
|       |-- history.html
|       |-- index.html
|       |-- map.html
|       |-- sighting.html
|       `-- zoo.html
|-- migrations
|   |-- README
|   |-- alembic.ini
|   |-- env.py
|   |-- script.py.mako
|   `-- versions
|       `-- fed7b412c063_initial_migrate.py
|-- tests
|   |-- conftest.py
|   |-- test_sightings
|   |-- functional
|   |   |-- __init__.py
|   |   |-- test_auth.py
|   |   `-- test_routes.py
|   |-- integration
|   |   |-- __init__.py
|   |   |-- test_config.py
|   |   `-- test_db.py
|    `-- unit
|       |-- __init__.py
|       |-- test_helpers.py
|       `-- test_models.py
|-- .env
|-- .env.template
|-- .flaskenv
|-- .gitignore
|-- .pre-commit-config.yaml
|-- config.py
|-- LICENSE
|-- poetry.lock
|-- pyproject.toml
|-- README.md
|-- requirements.txt
|-- setup.cfg
`-- wsgi.py
```

### groundhog - Project root

The following directory and files exist in the project root directory.

- .venv
- .env
- .env.template
- .flaskenv
- .gitignore
- .pre-commit-config.yaml
- config.py
- LICENSE
- poetry.lock
- pyproject.toml
- README.md
- requirements.txt
- setup.cfg
- wsgi.py

#### Environment and dependency management:

The `.venv` directory is not tracked nor uploaded to public repositories. However, I listed it here as an example. This is where Poetry stores my environment for development. Using a separate environment for each project allows me to keep my global workspace clean, use different versions of libraries for each project, and supply a valid `requirements.txt` or `poetry.lock` files for others to use.

The `.env` file contains secrets like passwords and API keys and should not be uploaded to public repositories! I have included a sample as `.env.template` as a way for people to get started quickly. They just need to add their specific information and remove `.template` from the file name. You can select your configuration via the environment by setting the config class in `CONFIG_TYPE` in .env and the class from `config.py`. The `config.py` shouldn't contain secrets either, so we can upload it to public repositories. This file allows you to have default configurations and build upon that via classes.

The `.flaskenv` file is used by Flask to setup environment variables that are needed such as `FLASK_APP` and `FLASK_DEBUG`, before the application is configured with the above mentioned `.env` file.

The `.gitignore` file is needed for projects tracked with Git. This file allows you to not upload temporary files, secrets, or caches that are in the project folder to the public repository.

The `.pre-commit-config.yaml` file is the configuration needed for the pre-commit package. This is the tool that executes the other tools e.g. Flake8, Black, and end of file checks on every commit. It can be manually run with the following command:

```
pre-commit run --all-files
```

The `config.py` file contains classes for creating configurations for different environments. This allows for configurations of different environments to be stored in a single file. It also gives the ability to inherit from the default class configuration. I chose this method, because it avoids having repetition in the multiple configurations.

The `LICENSE` file is created from the GitHub template for MIT licenses and specifies the usage of this project.

The `pyproject.toml` and `poetry.lock` files are created by Poetry. The `pyproject.toml` is a configuration file from Poetry, which contains the build information defined in PEP 518. That file contains the dependencies for the project. The `poetry.lock` file is created by Poetry and this 'pins' the versions defined in the `pyproject.toml` file. This should also be uploaded to public repositories so others can install the same version of dependencies that I used.

This `README.md` file is the current file. These are a common way to give information on the project, ex. installation or usage documentation.

The `requirements.txt` file are often still needed for builds such as GitHub Actions Continuous Integration and Continuous Delivery (CI/CD) or Platform As A Service (PaaS), such as Heroku or Render. Therefore Poetry allows for creating a `requirements.txt` file from the `poetry.lock`. To create this file, you can run this command:

```
poetry export --with dev --without-hashes --format=requirements.txt > requirements.txt
```

The `setup.cfg` file is the configuration file need for Flake8. For example, it has it excluded the migrations folder from being checked.

The `wsgi.py` file is the entry point for the application. This is often named app.py as well.

### .github - GitHub Actions Workflows

The directory .github\workflows contains YAML files for running GitHub actions. The current configruation builds the project and executes the unit tests. The `codecov.yml` file is used for configuring non-defaults for the coverage report for the project. The `dev_pipeline.yml` runs the CI on any commit to any branch -- other than the trunk branch. The `prod_pipeline.yml` runs the CI on any commit to the trunk branch. This workflow also creates and uploads a test report to [Codecov](https://about.codecov.io/). This allows for the usage of the Codecov badge at the top of this README.md. In the future this workflow would also include a CD component and deploy the app to a PAAS.

**.github**

- codecov.yml

**.github\workflows**

- dev_pipeline.yml
- prod_pipeline.yml

### groundhog - Module

- \_\_init\_\_.py
- auth.py
- helpers.py
- models.py
- routes.py

The `__init__.py` file is what creates the instance of the application. This is called by the wsgi.py file and is where plugins and Blueprints are registered.

The `auth.py` file contains the routes for registering, login, and logout functionalities.

The `helpers.py` file contains the decorator function for checking if the user is logged in.

The `models.py` file contains code for creating the tables and to be able to create, edit, delete records from the database.

The `routes.py` file contains the routes for the remaining pages of the application, such as Index/Home, Map, Zoo, Sighting, and Tracking History.

#### Static

- package-lock.json
- package.json

**css**

Compiled css from the sass `main.scss` file.

**images**

Contains all the images used in the application.

- groundhog_brand.png
- groundhog_main.jpeg
- groundhog_sighting.jpeg
- habitat_leaf.png
- seasons.png

**sass**

- main.scss

This `package-lock.json` and `package.json` files are for showing the version of Bootstrap that was installed during development. This was necessary in order to create the `main.scss` file. This contains the css for the project as well as the updating bootstrap default colors. This file is compiled and then put into the css folder as `main.min.css` and `main.min.css.map` for the application to use.

#### Templates

Contains the templates for the application.

- base.html
- history.html
- index.html
- map.html
- sighting.html
- zoo.html

This `base.html` file creates the basic structure html for all other templates. All other templates extend this template.

This `history.html` file is the template for the Tracking History page. This `index.html` file is the template for the main homepage. This `map.html` file is the template of the Map page. This `sighting.html` file is the template for the form in order to enter a sighting. This `zoo.html` file is the template for showing a list of zoos in the database.

**auth**

Contains the templates for the `auth` Blueprint.

- login.html
- register.html

This `login.html` file is the template for allowing a user to log into the application. This `register.html` file is the template for creating a new user in the application.

#### Migrations

- fed7b412c063_initial_migrate.py

The `fed7b412c063_initial_migrate.py` was created by using Flask Migrate when I initialized and created the initial database version. The rest of this folder was generated automatically by the Flask Migrate plugin.

### tests - Pytest Tests

The command to run all the tests, create a report as well as show the lines which are not yet covered is:

```
pytest --setup-show --cov=groundhog --cov-report term-missing
```

- conftest.py

**unit**

- \_\_init\_\_.py
- test_helpers.py
- test_models.py

**integration**

- \_\_init\_\_.py
- test_config.py
- test_db.py

**functional**

- \_\_init\_\_.py
- test_auth.py
- test_routes.py

The `conftest.py` file is used by Pytest and contains the setup and teardown code for the tests. The `test.db` isn't included in the repository as it is created only for some functional tests.

The `test_sightings` file is SQL that inserts some test sightings to the database.

I grouped the tests into two directories either `unit`, `integration`, or `functional` which was based on the level of the test.

The unit tests test the models with SQLAlchemy (not the database) `test_models.py`. The `test_helpers.py` tests the functions in the `helper.py` file.

The integration tests test configuring the application `test_config.py` or a PostgreSQL database in `test_db.py`. The functional tests test the user interactions.

The functional tests test the routes in the auth blueprint in `test_auth.py` and the `test_routes.py` test routes in routes blueprint.

## References:

### Technical References:

- [Flask application factory tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/)
- [Testing Flask applications](https://testdriven.io/blog/flask-pytest/)
- [The Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Github Actions examples](https://github.com/mgrum/flask-example-cicd/blob/main/.github/workflows/README.md)

### Groundhog References:

- [Ecology and Management of the Groundhog (Marmota monax)](https://njaes.rutgers.edu/e361/)
- The data for the [Habitat map](https://www.sciencebase.gov/catalog/item/58fa804ae4b0b7ea54525c0b) is provided by [U.S. Geological Survey (USGS) Gap Analysis Project (GAP), 2018, U.S.Geological Survey - Gap Analysis Project Species Range Maps CONUS_2001: U.S. Geological Survey data release, https://doi.org/10.5066/F7Q81B3R.](https://www.usgs.gov/programs/gap-analysis-project/science/species-data-web-services#overview)
- The data for the [Range map](https://www.sciencebase.gov/catalog/item/59f5e264e4b063d5d307de5d) is provided by [U.S. Geological Survey (USGS) Gap Analysis Project (GAP), 2018, U.S.Geological Survey - Gap Analysis Project Species Range Maps CONUS_2001: U.S. Geological Survey data release, https://doi.org/10.5066/F7Q81B3R.](https://www.usgs.gov/programs/gap-analysis-project/science/species-data-web-services#overview)
- The original picture for the index page `groundhog_main.jpeg` is found [here](https://pixabay.com/photos/animal-groundhog-mammal-wildlife-6716056/)
- The original picture for `groundhog_brand.png` is found [here](https://pixabay.com/photos/groundhog-groundhog-day-cute-animal-5946109/)
- The original picture for `groundhog_sighting.jpeg` is found [here](https://pixabay.com/photos/ground-hog-animal-groundhog-3745756/)
