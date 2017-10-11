import sys
from setuptools import setup

if sys.version_info.major < 3:
    sys.stderr.write("This package was made with Python 3. Continue at your own risk! \n")

setup(
    name='logtf_analyser',

    version='0.2',

    description='logtf_analyser is a cli app to download and query chat logs from Logs.tf. SQLite is required',

    url='https://github.com/cob16/tflog_analyzer',

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
    },

    entry_points={
        'console_scripts': [
            'logtf=logtf_analyser_cli.commands:logtf_analyser.start',
        ],
    },
)
