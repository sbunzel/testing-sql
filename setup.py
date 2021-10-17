from runpy import run_path

from setuptools import find_packages, setup

__version__ = run_path("src/testing_sql/version.py")["__version__"]

setup(
    name="testing_sql",
    version=__version__,
    author="Steffen Bunzel",
    packages=find_packages("src"),
    package_dir={"": "src"},
)
