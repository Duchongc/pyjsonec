#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 16:19
# @Author  : Anran
# @File    : setup.py
# @Function:

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjsonec",
    version="0.0.1",
    author="Anran",
    author_email="1978529954@qq.com",
    description="InterfaceUseCaseParameterExplosion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Duchongc/pyjsonec",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
