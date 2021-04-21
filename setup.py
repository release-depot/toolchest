#!/usr/bin/env python
# Copyright (c) 2018, Red Hat, Inc.
#   License: MIT
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


TEST_REQUIRES = ['coverage', 'flake8', 'pytest', 'pytest-datadir', 'tox']

setup(
    name='toolchest',
    version='0.0.8',
    install_requires=['pyyaml'],
    extras_require={'test': TEST_REQUIRES,
                    'docs': ['sphinx',
                             'sphinx-autobuild',
                             'sphinx-rtd-theme']},
    license='MIT',
    description=("toolchest is a collection of generic "
                 "functions for release-depot."),
    long_description=readme + '\n\n' + history,
    author='Red Hat',
    author_email='lhh@redhat.com',
    maintainer='Lon Hohberger',
    maintainer_email='lon@metamorphism.com',
    packages=find_packages(),
    url='http://github.com/release-depot/toolchest',
    data_files=[("", ["LICENSE"])],
    test_suite='tests',
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Utilities'],
)
