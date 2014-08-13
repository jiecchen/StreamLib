#!/usr/bin/env python

import os
import sys

import streamlib

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

short = 'A python library for streaming algorithms'
setup(
    name = 'streamlib',
    version = fn.__version__,
    description = short,
    long_description = open('README.md').read() + '\n\n' + open('CHANGES.txt').read(),
    author='Jiecchen',
    author_email='chenjiecao@gmail.com',
    url='https://github.com/jiecchen/StreamLib'
    packages=['streamlib', 'streamlib.sketch', 'streamlib.hashes'],
    package_data={'': ['LICENSE.txt', 'README.md', 'CHANGES.txt']},
    include_package_data=True,
    install_requires=[
        "mmh3 >= 2.0"
    ],
    license=open('LICENSE.txt').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
       # 'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
       # 'Programming Language :: Python :: 3',
       # 'Programming Language :: Python :: 3.1',
       # 'Programming Language :: Python :: 3.2',
       # 'Programming Language :: Python :: 3.3',
    ),
)
