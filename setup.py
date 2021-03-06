#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="check50_junit",
    version="0.5",
    author="Patrick Totzke",
    author_email="patricktotzke@gmail.com",
    description="A check50 extension for running "
                "and interpreting junit5 unit tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pazz/check50_junit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'check50',
        'check50_java',
    ],
    package_data={'check50_junit': ['lib/*.jar']},
)
