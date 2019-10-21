# Test REST Django

Django test project with DRF RESTful API

## Getting started

To install and run this project just create a python virtual enviroment and install the requetements in the file et/requirements.txt
All temporary files (under the folder tmp/ or with extension .tmp) are ignored
```
mkdir tmp
```

```
python3 -m venv tmp/venv
```

```
. tmp/venv/vin/activate
```

```
pip install -r etc/requirements.txt
```

### Note

The database is still in SQLite but it is not recommended to use this DBMS in production versions of a project

## The panel

In this project no custom views are implemented, so all objects must be administrated from the admin panel

## The API

The API responses are paginated, you can check the previous page and next page following the links provided in each response.
Pagination is set by default to 10, however you can modify the page length from the URL directly

### API response example
```
```

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org/) - Django toolkit to build Web APIs

## Authors

* **Adolfo Esparza** - *Initial work* - [aesparzas](https://github.com/aesparzas)

