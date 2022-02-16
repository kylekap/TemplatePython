# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Basic',
    version='0.1.0',
    description='Basic package for generating QR codes',
    long_description=readme,
    author='Kyle Patterson',
    url='https://github.com/kylekap/QRCodes',
    license=license,
    packages=find_packages(exclude=('Tests', 'Docs', 'Results'))
)

