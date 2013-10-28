#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Eve-Mongoengine',
    version='0.0.1',
    url='https://github.com/hellerstanislav/eve-mongoengine',
    author='Stanislav Heller',
    description='An Eve extension for Mongoengine ODM support',
    packages=['eve_mongoengine'],
    zip_safe=False,
    test_suite="tests",
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Eve>=0.1',
        'Flask>=0.10',
        'Mongoengine>=0.8.4',
    ]
)