# django_3_by_example
Follow along from the book Django 3 By Example

## Installation Instructions
* Install dependencies using `pip install -r requirements.txt`

## Creating a Project
* `django-admin startproject mysite`

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

## Create an application
* `python manage.py startapp blog`
* `blog/` - Application structure
  * `admin.py` - Register models to include them in the Django admin site
  * `apps.py` - Main configuration of the blog application
  * `migrations` - Directory contains database migrations - tracking model changes
  * `models.py` - Includes the data models of your applications. All Django apps must have a models.py file (but can be empty)
  * `tests.py` - Where to add tests to application
  * `views.py` - The logic of your application goes here - each view receives an HTTP request, processes it and returns a response

## Activate an application
* This allows Django to keep track of the application and be able to create database tables for the models.
To do the application add the new app (blog.apps.BlogConfig) to the INSTALLED_APPS setting.
* Then create and apply the migrations. This looks at all applications in INSTALLED_APPS and syncs the database
with the current models and existing migrations.

* Create an initial migration for the Post model.
  * `python manage.py makemigrations blog`
  * Check the SQL output from your first migration without executing using `python manage.py sqlmigrate blog 0001`
  * sync the databsase with the new model using `python manage.py migrate`
  * Upon every change to the models.py file you must create a new migration using `makemigrations`.
    This allows Django to keep track of all model changes. It must then be applied using `migrate` to keep the db in sync with the models
