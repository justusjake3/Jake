# Todo

## Pre requirements
* python 3.10
* poetry

## Setup
* `poetry install`

## Database Setup
Project requires a Postgres Database Setup in your machine

### Create Database
create a database 'todo' in your pgadmin app

### If different User
update sqlalchemy_url both in Alembic.ini and database.py

### Generating Migration
For migration
shell
alembic revision --autogenerate -m 'my message'

### Run Migration
To run migration
shell
alembic upgrade head

or for the case of downgrade
shell
alembic downgrade head


## Start dev API server
`ellar runserver --reload`

## API Docs
http://127.0.0.1:8000/docs