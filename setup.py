from setuptools import setup, find_packages

# Read the contents of your README file to use it for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-bls-api",
    version="0.1.0",
    author="Christopher Morris",  
    author_email="cmhope1986@gmail.com",
    description="A Python wrapper for the U.S. Bureau of Labor Statistics (BLS) API",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url="https://github.com/coding-with-chris/py-bls-api",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
        "pandas",
    ],
    python_requires=">=3.6",
    license="Proprietary"
)
