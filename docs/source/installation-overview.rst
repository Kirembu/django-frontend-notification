.. _installation-overview:

=====================
Installation overview
=====================

.. _install-requirements:

Install requirements
====================

A requirements file stores a list of dependencies to be installed for your project/application.

To get started with django-frontend-notification you must have the following installed:

- python >= 2.4 (programming language)
- Apache / http server with WSGI modules
- Django Framework >= 1.3 (Python based Web framework)



.. _install_requirements:

Install requirements
====================

Use PIP to install the dependencies listed in the requirments file,::

    $ pip install -r requirements.txt


.. _configuration:

Configuration
=============

Add ``frontend-notification`` into INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'frontend-notification',
        ...
        )

Add ``frontend_notification_tags`` into templates to use different template tags::

    {% load frontend_notification_tags %}

    {% get_notice_count request %}

To get count of notification in your django views, add ``notice_count``::

    ...
    from frontend_notification.views import notice_count
    ...

    def sample_view(request):
        print notice_count(request)

Download ``bootbox.js`` from bootboxjs.com_ and add into your media resource

.. _bootboxjs.com: http://bootboxjs.com/#download