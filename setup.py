from setuptools import setup, find_packages

setup(
    name="mypy_junitizer",
    version="0.0.1",
    url="https://www.cmsoftware.se",
    author="CM Software AB",
    author_email="development@cmsoftware.se",
    description="Script for converting output from MyPy to Junit XML format",
    packages=find_packages(),
    python_requires=">=3.9",
    entry_points={"console_scripts": ["mypy_junitizer = mypy_junitizer.mypy_junitizer:main"]},
    install_requires=['junit-xml', 'mypy', 'pydantic', 'sqlalchemy-stubs']
)
