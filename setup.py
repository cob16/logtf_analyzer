import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()

setup(
    python_requires='>=3',

    name='logtf_analyser',

    version='0.2.5',

    description='Downland and search chat logs from logs.tf',

    long_description=long_description,

    url='https://github.com/cob16/logtf_analyzer/',

    author='Cormac Brady',

    author_email='cormac.brady@hotmail.co.uk',

    license='MIT',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
    ],

    packages=[
        'logtf_analyser',
        'logtf_analyser_cli',
    ],

    install_requires=[
        'clint',
        'begins',
        'requests',
        'peewee'
    ],

    extras_require={
        'test': ['nose', 'parameterized'],
        'deploy': ['docutils', 'Pygments'],
    },

    entry_points={
        'console_scripts': [
            'logtf=logtf_analyser_cli.commands:logtf_analyser.start',
        ],
    },
)
