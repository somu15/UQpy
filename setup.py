#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='UQpy',
    version="2.0.1",
    url='https://github.com/SURGroup/UQpy',
    authors="Michael D. Shields, Dimitris G. Giovanis",
    author_emails="UQpy.info@gmail.com",
    license='MIT',
    platforms=["OSX", "Windows", "Linux"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["*.pdf"]},
    install_requires=[
        "numpy", "scipy", "matplotlib", "scikit-learn", 'fire'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
)
