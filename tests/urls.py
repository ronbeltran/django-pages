# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from pages.urls import urlpatterns as pages_urls

urlpatterns = [
    url(r'^', include(pages_urls, namespace='pages')),
]
