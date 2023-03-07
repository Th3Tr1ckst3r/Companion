# -*- coding: utf-8 -*-

# Learn more: https://github.com/Th3Tr1ckst3r/

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='sample',
    version='1.0',
    description='Sample package.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Adrian Tarver, Th3Tr1ckst3r',
    url='https://github.com/Th3Tr1ckst3r/',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: AGPT v3.0"
    ],
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "",
        "",
        ""
    ],
    
)

