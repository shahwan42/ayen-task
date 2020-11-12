# Ayen Task

Upload pdf & pptx files and search their names & contents.

## Run locally (On Ubuntu)

Prerequisites:

- Python3
- docker & docker-compose

Steps:

- install poetry: `$ pip install poetry`
- run `$ poetry install`
- copy `.env.example` to `.env`
- `$ docker-compose up` to run the database server
- `$ poetry shell` to activate the virtual environment
- `$ ./manage.py runserver` to run the development server
- open [http://localhost:8000/](http://localhost:8000/) to test the app manually
