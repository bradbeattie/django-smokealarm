Introduction
============

``django-smokealarm`` is a package designed to collect front-end JavaScript
errors and expose them in the admin backend for later inspection.

Requirements
============

Django 1.4 (it may work with older versions, but I haven't tested this)

Installation
============

Add ``smokealarm`` to your ``INSTALLED_APPS``.

Add smokealarm to your URLConf, using something like this::

  urlpatterns += patterns("",
      url(r"^smokealarm/", include("smokealarm.urls")),
  )

Add smokealarm to your base template, using something like this::

  <script src="{% static "js/smokealarm.js" %}"></script>
  <script>smokealarm_url = "{% url smokealarm_report %}";</script>


Usage
=====

As JavaScript errors occur in the front end, browsers will make posts to
the smokealarm_report URL. The subsequently created models are available
in your backend admin.
