###############################################################################
                             TASK MANAGER SERVICE
###############################################################################

This is a training project made in addition to the `Python training course`_.
This is done using the `Django`_ framework and demonstrates its abilities. And
yes, this is another "todo app" on the internet.

.. _Python training course: https://github.com/shorodilov/python-course.git
.. _Django: https://djangoproject.com/

Getting started
===============

Download the code base on your local machine. You may prefer to use virtual
environment to separate the project's dependencies from other packages you
have installed.

To install dependencies use ``pip`` or `poetry`_:

.. code-block::

    pip install -r requirements.txt

.. code-block::

    poetry install

After downloading the project, set the required environment variables. Refer
the table in `Environment variables`_ section for more information.

To run the project do

.. code-block::

    python manage.py runserver

The output should look like:

::

    Starting development server at http://127.0.0.1:8000/

Visit the printed out address in your web-browser to see the running webapp.

.. _poetry: https://python-poetry.org/

Environment variables
=====================

The project requires some environment variables defined. To set up an environ
variable do:

.. code-block::

    set VARIABLE_NAME=VARIABLE_VALUE     # windows
    export VARIABLE_NAME=VARIABLE_VALUE  # macos or linux

See the table of variables used within this project below.

+----------------------------+------------------------------------------------+
| Variable name              | Variable description                           |
+============================+================================================+
| ``DJANGO_SECRET_KEY``      | The secret key is required by Django security  |
|                            | middleware. For the security reasons this can  |
|                            | not be shared across the internet, and should  |
|                            | be setup for each project individual instance  |
|                            | separately. Here is a good service to get it:  |
|                            | https://djecrety.ir/                           |
+----------------------------+------------------------------------------------+
