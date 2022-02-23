import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple_coverage",
    version="0.3.2",
    author="Nikolai Limbrunner",
    author_email="nikolai.limbrunner@gmail.com",
    description="Simple Coverage measurements for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikolim/simple-coverage",
    package_dir={"simple_coverage": "simple_coverage"},
    packages=["simple_coverage"],
    python_requires=">=3.6",
    install_requires=["termcolor"],
)
