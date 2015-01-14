import os

from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='manipuldate',
    version='0.2.0',
    description='Date/Time/DateTime Manipulation Done Right',
    long_description=read('.', 'ReadMe.md'),
    url='https://github.com/JenkinsDev/manipuldate',
    license='MIT',
    author='David Jenkins',
    author_email='david.nicholas.jenkins@gmail.com',
    packages=['manipuldate', ],
    install_requires=[
        'enum34',
    ],
    include_package_data=True,
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
