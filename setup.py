from setuptools import setup

requires = ["leveldb>=0.193", "numpy>=1.8.2", "spacy>=1.6.0", "unidecode>=0.4.19", "nltk>=3.3.0"]

setup(
    name="quickumls",
    version="1.0",
    description="Fork from https://github.com/Georgetown-IR-Lab/QuickUMLS",
    packages=["quickumls.core", "quickumls.simstring"],
    install_requires=requires,
    package_data={'quickumls.simstring': ['_simstring.cpython-36m-x86_64-linux-gnu.so']},
    include_package_data=True,
)
