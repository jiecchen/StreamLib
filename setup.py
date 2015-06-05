# coding=utf-8
from setuptools import setup, find_packages
from codecs import open
import os


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return open(path, encoding='utf-8').read()


setup(
    name="streamlib",
    version="1.0.1",
    packages=find_packages(),

    # development metadata
    zip_safe=True,

    # metadata for upload to PyPI
    author="Jiecao Chen",
    author_email="chenjiecao@gmail.com",
    description="TinyDB is a tiny, document oriented database optimized for "
                "your happiness :)",
    license="MIT",
    keywords="streaming algorithms",
    url="https://github.com/jiecchen/StreamLib",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Researchers",
        "Intended Audience :: Data Scientists",
        "License :: OSI Approved :: MIT License",
        "Topic :: Algorithms",
        "Topic :: Algorithms :: Streaming Algorithms",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
#        "Programming Language :: Python :: 3.3",
#        "Programming Language :: Python :: 3.4",
#        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ],

    long_description=read('README.md'),
    install_requires=[
        'mmh3',
    ],
)

