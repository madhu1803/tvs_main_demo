# TVS Forms

## Prerequesties

1. Python3
2. Virtualenv

## Getting started

1. Make sure that you set the db details in app.py and follow the db struture given.
2. `virtualenv -p python3 venv`
3. `pip install -r requirements.txt`
4. `python app.py`

## DB Structure

1. The database should contain three tables `form1`, `form2` and `form3`.
2. Each table should contain the following:  
   a. `id` not null, primary key, unique, auto increment  
   b. `date` not null, DATE, current date
