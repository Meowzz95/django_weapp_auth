import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-weapp-auth',
    version='1.0.6',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A helper Django app that handles wechat mini program login and user info updating logic',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://blog.mimimi.fun/',
    author='Meowzz95',
    author_email='info@mimimi.fun',
    install_requires=[
          'requests',
          'pycrypto'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)