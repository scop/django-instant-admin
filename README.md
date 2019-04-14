# Django instant admin

This is a skeleton setup for creating a Django admin site for an
existing database. The existing database schema is not modified, and
data needed by Django's admin site directed to another (by default
SQLite) database.

## Setup

1. Install dependencies:  
   `pip install -r requirements.txt`
1. Install driver for your database:  
   https://docs.djangoproject.com/en/2.2/ref/databases/
1. Set environment variables:  
  `SECRET_KEY`: https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECRET_KEY  
  `DATABASE_URL`: URL to the inspected database, see https://github.com/kennethreitz/dj-database-url#url-schema
1. Prepare instant-admin database:  
   `./manage.py migrate`
1. Create a super user:  
   `./manage.py createsuperuser`
1. Generate models for inspected database:  
   `./manage.py inspectdb --database inspected > inspected/models.py`
1. Start the development server:  
   `./manage.py runserver`

At this point, depending on the underlying database structure and how
good a job Django's inspectdb does with it, you may have a working
Django admin site ready to be used against the inspected database. Log
in at the URL given in the console using the super user account
created above.

There may be some more or less cosmetic tweaks you may want to make to
the model, for example changing some `IntegerField`s to
`BooleanField`s, adding `ordering` to models' `Meta` classes etc.

It may also be that you'll receive error spewage on the console at
startup which you'll need to fix before the admin site will
work. Typically, these fixes need to be made in `inspected/models.py`
only.
