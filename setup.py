from setuptools import setup, find_packages

setup(
    name="protein-variant-nomenclature-parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "antlr4-python3-runtime>=4.8,<5.0",
    ],
)
