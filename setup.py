#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Tomas Johansson",
    author_email='pypi@programmerare.com',
    python_requires='>=2.7, < 3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Topic :: Scientific/Engineering :: GIS",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python library for transformation of geographic coordinates between WGS84 and the Swedish coordinate reference systems SWEREF99 and RT90",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='sweden_crs_transformations',
    name='sweden_crs_transformations-programmerare',  # name at 'test.pypi.org'
    # name='sweden_crs_transformations',  # name at 'pypi.org'
    packages=find_packages(include=['sweden_crs_transformations', 'sweden_crs_transformations.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/TomasJohansson/sweden_crs_transformations_4python',
    version='0.1.0',
    zip_safe=False,
)
