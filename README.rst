=============================
Django Pages
=============================

.. image:: https://badge.fury.io/py/django-pages.svg
    :target: https://badge.fury.io/py/django-pages

.. image:: https://travis-ci.org/ronbeltran/django-pages.svg?branch=master
    :target: https://travis-ci.org/ronbeltran/django-pages

.. image:: https://codecov.io/gh/ronbeltran/django-pages/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ronbeltran/django-pages

Add pages to a django site quickly with flatpages app and ckeditor

Documentation
-------------

The full documentation is at TODO: https://django-pages.readthedocs.io.

Quickstart
----------

Install the Django flatpages app

https://docs.djangoproject.com/en/1.11/ref/contrib/flatpages/

Install Django Pages::

    pip install -e git+https://github.com/ronbeltran/django-pages@master#egg=django-pages

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pages.apps.PagesConfig',
        ...
    )

Add Django Pages's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        url(r'^pages/', include('django.contrib.flatpages.urls')),
        url(r'^ckeditor/', include('ckeditor_uploader.urls')),
        ...
    ]

 Add in settings

.. code-block:: python

    CKEDITOR_UPLOAD_PATH = "uploads/"
    CKEDITOR_IMAGE_BACKEND = "pillow"

For more details and customization with the ckeditor please see `django-ckeditor`_


Override admin template to add ckeditor references: templates/admin/base_site.html

.. code-block:: python

    {% extends "admin/base_site.html" %}

    {% block extrahead %}
    <script>window.CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/';</script>
    {{ block.super }}
    {% endblock %}

Make sure you have run the ff:

.. code-block:: sh

    python manage.py migrate
    python manage.py collectstatic --noinput


Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _`django-ckeditor`: https://django-ckeditor.readthedocs.io/en/latest/index.html
