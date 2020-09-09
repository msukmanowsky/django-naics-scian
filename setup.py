#!/usr/bin/env python3
import os
import sys
import re

from setuptools import find_packages, setup


def get_version(package):
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name="django_naics_scian",
    version=get_version("naics_scian"),
    url="https://github.com/msukmanowsky/django-naics-scian",
    license="BSD",
    description="Tables for the North American Industry Classification System (NAICS)",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mike Sukmanowsky",
    author_email="mike.sukmanowsky@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=("django>=2.2",),
    python_requires=">=3.5",
    zip_safe=False,
    classifiers=[
        # 'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
    ],
    project_urls={"Source": "https://github.com/msukmanowsky/django-naics-scian"},
)
