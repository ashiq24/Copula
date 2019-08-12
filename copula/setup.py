import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="copula",
    version="0.0.4",
    author="Md Ashiqur Rahman",
    author_email="ashiqbuet14@gmail.com",
    description="A python library for sampling and generating new Data points by multivariate Gaussian copulas.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashiq24/Copula",
    packages=["copula"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)