from setuptools import setup, find_packages

setup(
    name='nandhatest',
    version='1.0.0',
    author='test',
    description='Function which file upload and download the files to the specified bucket',
    author_email='nanthakumar.ananthan@innoboon.com',
    packages=find_packages(),
    install_requires=[
        'google-cloud-storage',
        'boto3',
        'botocore',
        'selenium',
        'webdriver-manager',
        'Scrapy',
    ],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10.6',
    ],
)