from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Gavl", # Replace with your own username
    version="1.0.1",
    author="Ignacio Garrido Botella",
    author_email="igngarridobotella@gmail.com",
    description="Framework to launch a genetic algorithm with chromosomes with variable length.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IgnacioGarrido/Gavl.git",
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    )
