# Mozio

### Requirements

- Python 3.7 or higher

### Setup

Create virtual environment and activate it. <br/>

```sh
python -m venv app
```

install requirements

```sh
pip install -r requirements/requirements.txt
```

update database details in <strong>"config/settings/settings.py"</strong>

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": (Name of database), 
        "USER": (Username),
        "PASSWORD": (Password),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

migrate database
```sh
python manage.py migrate
```

run application
```
python manage.py runserver
```

### API Endpoints

- /mozio_api/ - Base api endpoint with list of available endpoints 
- /mozio_api/providers/ - Provider endpoint
- /mozio_api/service_areas/ - ServiceArea endpoint with optional query params ex:
  - /mozio_api/service_areas/?longitude=122.22&latitude=133.55
