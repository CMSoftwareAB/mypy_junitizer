import re

from setuptools import setup


with open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="mypy_junitizer",
    version="0.0.1",
    url="https://github.com/CMSoftwareAB/mypy_junitizer",
    license="BSD-3-Clause",
    author="Giovanni Gibelli",
    author_email="giovanni@callmaker.se",
    description="Script for converting output from MyPy to Junit XML format",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    py_modules=["mypy_junitizer"],
    python_requires=">=3.5",
    entry_points={"console_scripts": ["mypy_junitizer = mypy_junitizer:main"]},
    install_requires=['junit-xml']
)
