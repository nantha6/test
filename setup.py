from setuptools import setup, find_packages

setup(
    name='nandhatest',
    namespace_package=['nandhatest'],
    version='1.0.0',
    author='nandha',
    description='Function which file upload and download the files to the specified bucket',
    author_email='nanthakumar.ananthan@innoboon.com',
    packages=find_packages(),
    url='https://github.com/nantha6/test',
    install_requires=[
        'boto3'
    ]
)