# Task TEB-team

**How to run localy?**

Clone the repository using
```
git clone https://github.com/sazzeck/Task--TEB-team-
poetry shell
poetry install
```

First of all check `.env.example` for Examples on environment variables.

```
BOT_TOKEN = str:<TELEGRAM_BOT_TOKEN>

SECRET_KEY = str:<DJANGO_SECRET_KEY>

DB_NAME = str:<DATABASE_NAME>
DB_USER = str:<DATABASE_USER>
DB_PASSWORD = str:<DATABASE_PORT>
DB_HOST = str:<DATABASE_HOST>
DB_PORT = str:<DATABASE_PORT>

AIRTABLE_API_KEY = str:<AIRTABLE_API_KEY>
AIRTABLE_BASE_ID = str:<AIRTABLE_BASE_ID>
AIRTABLE_TABLE_NAME = str:<AIRTABLE_TABLE_NAME>
```


After cloning and setting `.env`
```
cd app

./manage.py makemigrations
./manage.py migrate
```

Can run
```
./manage.py runserver
```
