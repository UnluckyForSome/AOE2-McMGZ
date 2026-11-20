"""Setup."""
from setuptools import setup, find_packages

setup(
    name='AOE2-McMGZ',
    version='0.1.0',
    description='Museum-maintained fork of mgz for parsing Age of Empires II recorded games.',
    url='https://github.com/UnluckyForSome/AOE2-McMGZ',
    license='MIT',
    author='happyleaves',
    author_email='happyleaves.tfr@gmail.com',
    packages=find_packages(),
    install_requires=[
        'aocref>=2.0.35',
        'construct==2.8.16',
        'dataclasses==0.8; python_version < "3.7"',
        'tabulate>=0.9.0',
    ],
    entry_points = {
        'console_scripts': ['mgz=mgz.cli:main'],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
