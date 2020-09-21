from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="quickmongo.py",
    version="0.0.1",
    description="A simple and quick wrapper for pymongo!",
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=['quickmongo'],
    keywords="quickmongo.py",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    license="MIT",
)