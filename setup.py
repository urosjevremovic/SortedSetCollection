"""
SortedSet
-------------

Implementation of Immutable Sorted Set collection.

You can get it by downloading it directly or by typing:

.. code:: bash

    $ pip install SortedSet

After it is installed you can start it by simply typing in your terminal:

.. code:: bash

    $ SortedSet(['list_of_integer_data'])

For example

.. code:: bash

    $ SortedSet([1, 2, 5, 3, 3, 1])

Would return the following

.. code:: bash

    $ {1, 2, 3, 5}

"""

from setuptools import setup

setup(name='SortedSet',
      version='0.1',
      description='Implementation of Immutable Sorted Set collection',
      long_description=__doc__,
      long_description_content_type='text/markdown',
      url="https://github.com/urosjevremovic/txt-file-size-checker",
      license='MIT',
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['TextFileSizeChecker'],
      entry_points={
          "console_scripts": ["size-checker=TextFileSizeChecker.txt_file_size_checker:main"],
      },
      )

__author__ = 'Uros Jevremovic'