# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "morfinator_api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="The Morfinator",
    author_email="giscraig@gmail.com",
    url="",
    keywords=["Swagger", "The Morfinator"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['morfinator_api=morfinator_api.__main__:main']},
    long_description="""\
    API for weekly meal generator app.
    """
)

