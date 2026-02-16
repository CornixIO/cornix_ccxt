from setuptools import setup, find_packages

setup(
    name='cornix_ccxt',
    version='1.0.14',
    packages=find_packages(),
    install_requires=[
        'ccxt==4.5.38',
    ],
)
