from setuptools import setup, find_packages
from Cython.Build import cythonize
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()

setup(
    name="streamlib",
    version="0.0.1",
    url="none",
    author="Jiecao Chen",
    author_email="chenjiecao@gmail.com",
    packages=find_packages(),
    ext_modules=cythonize("streamlib/*.pyx"),
    long_description=read('README.rst'),
    install_requires=['mmh3'],
)
