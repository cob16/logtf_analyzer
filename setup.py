import sys
from setuptools import setup

if sys.version_info.major < 3:
    sys.stderr.write("This package was made with Python 3. Continue at your own risk! \n")

setup(
    name='logtf_analyser_cli',

    version='0.1',

    description='Logs.tf chat analyser',

    # The project's main homepage.
    # url='https://github.com/pypa/sampleproject',

    author='cormac brady',
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
    ],

    extras_require={
        'test': ['nose'],
    },

    entry_points={
        'console_scripts': [
            'logtf=logtf_analyser_cli.commands:logtf_analyser.start',
        ],
    },
)
