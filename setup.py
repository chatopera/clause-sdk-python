# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from clause import __version__

with open("README.md", "r") as fh:
    long_description = '''
中文语义理解服务 Python SDK
----------------------------
https://github.com/chatopera/py-clause/
'''

setup(
    name='clause',
    version=__version__,
    description='中文语义理解服务 Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hai Liang Wang',
    author_email='hain@chatopera.com',
    url='https://github.com/chatopera/py-clause',
    license="Apache Software License",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'],
    keywords='chatbot,machine-learning,NLU,NLP',
    packages=find_packages(),
    install_requires=[
        "absl-py>=0.8",
        "thrift==0.11.0"
    ],
    package_data={
        'clause': [
            '**/*.gz',
            '**/*.txt',
            '**/*.vector',
            'LICENSE']})
