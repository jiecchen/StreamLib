# coding=utf-8
from setuptools import setup, find_packages
from codecs import open
import os
from distutils.core import setup, Command

def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()

# class PyTest(Command):
#     user_options = []
#     def initialize_options(self):
#         pass
#     def finalize_options(self):
#         pass
#     def run(self):
#         import sys,subprocess
#         errno = subprocess.call([sys.executable, 'runtests.py'])
#         raise SystemExit(errno)



setup(
    name="StreamLib",
    version="1.0.1",
    packages=find_packages(),

    # development metadata
    zip_safe=True,

    # metadata for upload to PyPI
    author="Jiecao Chen",
    author_email="chenjiecao@gmail.com",
    description="StreamLib: Library of streaming algorithms ",
    license="MIT",
    keywords="Streaming Algorithms",
    url="https://github.com/jiecchen/StreamLib",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
#        "Programming Language :: Python :: 3.3",
 #       "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ],

    long_description=read('README.md'),
    install_requires=['mmh3'],
#    cmdclass = {'test': PyTest},
)
