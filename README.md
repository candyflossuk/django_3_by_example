# django_3_by_example
Follow along from the book Django 3 By Example

## Installation Instructions
* Install dependencies using `pip install -r requirements.txt`

## Running Migrations
* `cd mysite`

* ` python manage.py migrate`

## Start Development Server
* `python manage.py runserver`

To run with a custom host, port or use a specific settings file use the following
* `python manage.py runserver 127.0.0.1:8001 \--settings=mysite.settings`

## Django Project Structure
* `manage.py` - Thin wrapper around `django-admin.py`
* `mysite/` - Project directory 
    * `__init__.py` - Tells Python to treat the mysite directory as Python module
    * `asgi.py` - Configuration to run project as ASGI (Python standard for async web servers and apps)
    * `settings.py` - Settings and config for project and contains default settings
    * `urls.py` - Where URL patterns live. Each URL is mapped to a view
    * `wsgi.py` - Config to run your project as a WSGI application
