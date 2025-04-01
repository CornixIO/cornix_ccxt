from setuptools import setup, find_packages

setup(
    name='cornix_ccxt',
    version='1.0.9',
    packages=find_packages(),
    install_requires=[
        'ccxt @ https://github.com/CornixIO/ccxt/archive/refs/tags/4.0.106.95.tar.gz#subdirectory=python',
    ],
)
