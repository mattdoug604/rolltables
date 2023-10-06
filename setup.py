from setuptools import find_packages, setup

setup(
    name="rolltables",
    version="0.2.0",
    author="Matt Douglas",
    author_email="mattdoug604@gmail.com",
    packages=find_packages(),
    description="A flexible Python package for creating and using random tables with your favorite TTRPG.",
    python_requires=">=3.6",
    install_requires=["Jinja2"],
    include_package_data=True,
    extras_require={"dev": ["black", "isort", "mypy"], "tests": ["pytest", "pytest-mock"]},
    entry_points={"console_scripts": ["rolltables=rolltables.main:main"]},
)
