#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='choosealicense',
    version='0.1.0',
    description="Choose a License is a Cookiecutter plugin for selecting an open-source license.",
    long_description=readme + '\n\n' + history,
    author="Audrey Roy Greenfeld",
    author_email='aroy@alum.mit.edu',
    url='https://github.com/audreyr/choosealicense',
    packages=[
        'choosealicense',
    ],
    package_dir={'choosealicense':
                 'choosealicense'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='choosealicense',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
