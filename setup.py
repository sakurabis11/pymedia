from setuptools import setup, find_packages

setup(
    name='pinterest_image_downloader',
    version='0.1.0',
    description='A Python library for downloading images from Pinterest',
    author='Amal nath',
    author_email='your_email@example.com',
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
)
