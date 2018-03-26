=============================
pychargifysimple
=============================

.. image:: https://img.shields.io/pypi/v/pychargifysimple.svg
   :alt: Latest release on the Python Cheeseshop (PyPI)
   :target: https://pypi.python.org/pypi/pychargifysimple

A simple wrapper for chargify. Provide also a module to have interaction with
the website and provide for example the possibility to delete a subscription.

Documentation
-------------

The full documentation is at https://pychargifysimple.readthedocs.io.

Quickstart
----------

Install pychargifysimple::

    pip pychargifysimple

Example:

.. code-block:: python

    from pychargifysimple.web import ChargifyWeb

    chargify_web = ChargifyWeb(
        user='your_user', password='your_password',
        url='your_url')
    chargify_web.delete_subscription(42)


Initialize a ChargifyWeb object and remove a subscription.

Features
--------

* Possibility to remove subscription
