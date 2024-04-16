"""Setup file for the project."""

from setuptools import find_packages, setup

packages_to_install = ["setuptools", "wheel", "boto3"]

setup(
    name="build_pre_commit_hooks",
    version="0.1",
    url="",
    license="",
    author="Anthony Pernia",
    author_email="anthonyperniah@gmail.com",
    description="",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=packages_to_install,
)