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

#### Note

The database is still in SQLite but it is not recommended to use this DBMS in production versions of a project

## The panel

In this project no custom views are implemented, so all objects must be administrated from the admin panel

## The API

The API responses are paginated, you can check the previous page and next page following the links provided in each response.
Pagination is set by default to 10, however you can modify the page length from the URL directly

#### API Authorization

The API consumption is restricted by a Token that can be generated in the api-token-auth/ endpoint providing a username and a password in the body of a POST request. After Token is generated, it will expire in 15 days and it is needed to be used as a header of the request in the following way:

```
Authorization: Token abc123
```

#### API Endpoints

The endpoint house/ is operating and acepting GET and POST requests. Fur retrieving, updating and deleting you have to use the slug and GET, PATCH and DELETE methods.

#### API response example
```
{
    "user": null,
    "next": null,
    "previous": null,
    "count": 2,
    "products": [
        {
            "name": "Universidad",
            "address": "Av. Universidad 1952",
            "surface": "200.00",
            "contact_email": "con@tacto.com",
            "slug": "380CA2"
        },
        {
            "name": "Jardin",
            "address": "Av Jardin 330",
            "surface": "100.00",
            "contact_email": "con@tacto.com",
            "slug": "EF1DC1"
        }
    ]
}
```

#### API Request Logging

All requests to the API are registered in a request.log file that can be found in src/ directory once the project is serving

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org/) - Django toolkit to build Web APIs

## Authors

* **Adolfo Esparza** - *Initial work* - [aesparzas](https://github.com/aesparzas)

