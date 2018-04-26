#!/usr/bin/env python
# coding=utf-8

"""
python distribute file
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

from setuptools import setup, find_packages

pkg_name = "reinforcement-learning-py"
pkg_version = "0.1.0"

def requirements_file_to_list(fn="requirements.txt"):
    """read a requirements file and create a list that can be used in setup.

    """
    with open(fn, 'r') as f:
        return [x.rstrip() for x in list(f) if x and not x.startswith('#')]

setup(
    name=pkg_name
    version=pkg_version
    packages=find_packages(),
    install_requires=requirements_file_to_list(),
    dependency_links=[
        # If your project has dependencies on some internal packages that is
        # not on PyPI, you may list package index url here. Then you can just
        # mention package name and version in requirements.txt file.
    ],
    entry_points={
        # 'console_scripts': [
        #     'main = ' + pkg_name + '.main:main',
        # ]
    },
    package_data={
        pkg_name : ['logger.conf']
    },
    author="Gustavo Kuhn Andriotti",
    author_email="gustavo.andriotti@gmail.com",
    maintainer="",
    maintainer_email="",
    description="A Python port of https://github.com/dbatalov/reinforcement-learning",
    long_description=open('README.rst').read(),
    license="MIT",
    url="https://pypi.python.org/pypi/" + pgk_name,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: The MIT License (MIT)'
        'Programming Language :: Python :: 3.6',
    ]
)
