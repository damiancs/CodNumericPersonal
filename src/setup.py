# coding=utf-8
"""
Setup file for CNP module.
"""

import os
from setuptools import setup


def read_file(file_name):
    """
    Utility function to read the README file.
    Used for the long_description.  It's nice, because now:
    1) we have a top level README file;
    2) it's easier to type in the README file than to put a raw string in below.
    :param file_name: the name of the file to read.
    :type file_name: str | unicode
    :return: A file instance.
    :rtype: file
    """
    return open(os.path.join(os.path.dirname(os.path.dirname(__file__)), file_name)).read()


setup(
    name="CodNumericPersonal",
    version="0.0.1",
    author="Sebastian Dămian",
    author_email="develop@damiancs.ro",
    description="A CNP validator.",
    license="MIT",
    keywords="cod numeric personal cnp",
    url="https://github.com/damiancs/CodNumericPersonal",
    packages=['CodNumericPersonal'],
    long_description=read_file('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "Programming Language :: Python"
    ],
)
