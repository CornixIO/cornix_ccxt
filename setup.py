from setuptools import setup, find_packages

setup(
    name='cornix_ccxt',
    version='1.0.8',
    packages=find_packages(),
    install_requires=[
        'ccxt==4.4.98',
    ],
)
