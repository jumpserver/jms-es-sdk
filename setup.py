# -*- coding: utf-8 -*-
#
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('jms_es_sdk/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='jms-es-sdk',
    version=version,
    description='Jumpserver elastic search storage sdk',
    long_description=readme,
    keywords='jumpserver elastic storage',
    packages=['jms_es_sdk'],
    author='Jumpserver team',
    author_email='ibuler@qq.com',
    install_requires=[
        'elasticsearch==6.1.1'
    ],
    include_package_data=True,
    url='http://jumpserver.org',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
