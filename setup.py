import io
from setuptools import setup, find_packages


def requirements():
    with io.open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = f.read()
    return requirements

setup(
    name="mlopslib",
    version="0.0.1",
    description="custom library for ml",
    url="https://github.com/wonyoungseo/fc-mlops-library",
    author="wyseo",
    packages=["mlopslib"],
    install_requires=requirements()
)