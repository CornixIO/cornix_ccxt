from setuptools import setup, find_packages

setup(
    name='cornix_ccxt',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'ccxt @ https://github.com/CornixIO/ccxt/archive/refs/tags/4.0.106.82.tar.gz#subdirectory=python',
    ],
)
