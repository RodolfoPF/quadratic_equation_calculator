from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="quadratic_equation_calculator",
    version="0.0.1",
    author="Rodolfo",
    author_email="rodolfo.pereiraf1@outlook.com",
    description="Program to calculate a quadratic equation",
    url="https://github.com/RodolfoPF/quadratic_equation_calculator"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)