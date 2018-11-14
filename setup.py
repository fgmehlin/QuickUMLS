from setuptools import setup, PEP420PackageFinder

requires = [
    "leveldb>=0.193",
    "numpy>=1.8.2",
    "spacy>=1.6.0",
    "unidecode>=0.4.19"
    ]

setup(
    name="quickumls",
    version="1.0",
    description="Fork from https://github.com/Georgetown-IR-Lab/QuickUMLS",
    packages=["quickumls", "simstring"],
    install_requires=requires,
)