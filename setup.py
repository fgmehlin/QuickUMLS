from setuptools import setup

requires = [
    "leveldb>=0.193",
    "numpy>=1.8.2",
    "spacy>=1.6.0",
    "unidecode>=0.4.19"
    ]

setup(
    name="quickumls",
    version="1.0",
    description="Forked from https://github.com/Georgetown-IR-Lab/QuickUMLS",
    author="Floran Gmehlin",
    author_email="email@domain.gosu",
    url="https://github.com/fgmehlin/QuickUMLS",
    zip_safe=False,
    install_requires=requires,
)