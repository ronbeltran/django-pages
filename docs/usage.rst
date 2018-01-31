=====
Usage
=====

To use Django Pages in a project, add it to your `INSTALLED_APPS`:

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
