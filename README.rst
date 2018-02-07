Autonomie base software
=======================

.. image::
    https://secure.travis-ci.org/CroissanceCommune/autonomie_base.png?branch=master
   :target: http://travis-ci.org/CroissanceCommune/autonomie_base
   :alt: Travis-ci: continuous integration status.

Provide :

* common models
* common tools

This package provides base tools to allow splitting the software Autonomie in several pieces.
It provides :

* SQLAlchemy configuration (scoped session, base model class)
* Custom SQLAlchemy column types
* String formatting utilities
* Date formatting utilities
* Constants
* ...

It should not be installed directly but should be installed as a dependency
