.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

===============
dsgov.migration
===============

Migrates content from SimpleJSON format to Plone 5

Documentation
-------------
This component is being developed following the guidelines documented in:
- https://training.plone.org/5/transmogrifier/.


Installation In Production
------------

This component is still under development,
for now the installation can be done by cloning this directory
inside the src folder of your website and configuring the buildout to
fetch the package from there. Or you can upload your site using the
buildout available here.

At the end of the [buildout] session in your buildout.cfg
Insert the following code like::
   [buildout]
   ...

   auto-checkout = *
   [sources]
   dsgov.migration = git https://gitlab.ifrr.edu.br/2045293/dsgov.migration

   ...

Run buildout::

    $ buildout


Installation In Development
------------

Set up a virtual environment using python 3.8

Then run the command::

    $ pip install -r requirements.txt

Run buildout::

    $ buildout

Start Plone in foreground::

    $ instance fg

Contribute
----------

- Issue Tracker: https://github.com/f4biosa/dsgov.migration/issues


License
-------

The project is licensed under the GPLv2.
