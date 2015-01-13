#!/usr/bin/env python

from setuptools import setup
from aiowmata import __version__

long_description = "AsyncIO WMATA bindings"

setup(
    name="aiowmata",
    version=__version__,
    packages=['aiowmata',],
    author="Paul Tagliamonte",
    author_email="paultag@gmail.com",
    long_description=long_description,
    description='does some stuff with things & stuff',
    license="Expat",
    url="",
    platforms=['any']
)
