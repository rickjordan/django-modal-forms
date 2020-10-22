import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-modal-forms',
    version='2.0',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    license='MIT License',
    description='Django Forms in Bootstrap Modals',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/rickjordan/django-modal-forms',
    author='Rick Jordan',
    author_email='jordan.rick.d@gmail.com',
    install_requires=[
        'django-widget-tweaks',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
