"""
For checking developing environment
"""
# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import warnings
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup


def get_readme():
    """
    Get the README from the current directory. If there isn't one, return an empty string.
    """
    all_readmes = sorted(glob('README*'))
    if len(all_readmes) > 1:
        warnings.warn(
            'There seems to be more than one README in this directory. Choosing the '
            'first in lexicographic order.',
        )
    if len(all_readmes) > 0:
        return open(all_readmes[0], 'r', encoding='UTF-8').read()

    warnings.warn("There doesn't seem to be a README in this directory.")
    return ''


setup(
    name='example',
    version='1.0',
    license='MIT',
    description='description',
    long_description='\n' + get_readme(),
    author='Kevin Wu',
    author_email='admin@kevinw.net',
    packages=find_packages('app_package'),
    package_dir={'': 'app_package'},
    # install_requires=[''], #external packages as dependencies
    py_modules=[splitext(basename(path))[0] for path in glob('app_package/**/*.py')],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.11',
    setup_requires=[
        'pytest-runner',
    ],
)
