#!/usr/bin/env python

""" The setup script."""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = [x for x in f.read().split('\n') if x.strip()]

setup(
    name='cli_tool',
    use_scm_version=True,
    description='CLI Tools Interface',
    long_description=readme + '\n\n' + history,
    author='Arib Hussain',
    author_email='ahussa76@ford.com',
    url='',
    packages=find_packages(include=['cli_tool']),
    include_package_data=True,
    zip_safe=False,
    keywords='cli_tool',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'cli=cli_tool.cli:main'
        ]
    }
)