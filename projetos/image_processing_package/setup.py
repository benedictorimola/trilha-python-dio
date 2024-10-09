from setuptools import setup, find_packages

with open("README.md","r") as f:
    page_description = f.read()
    
with open("requiriments.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Benedicto Rimola",
    author_email="rimolabenedicto@gmail.com",
    description="Criando imagens com marca d´água",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my git url",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5"
)