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

Install Django Pages::

    pip install django-pages

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'pages.apps.PagesConfig',
        ...
    )

Add Django Pages's URL patterns:

.. code-block:: python

    from pages import urls as pages_urls


    urlpatterns = [
        ...
        url(r'^', include(pages_urls)),
        ...
    ]

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
