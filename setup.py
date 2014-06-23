from setuptools import setup, find_packages
import os

base = os.path.dirname(__file__)
local = lambda x: os.path.join(base, x)


def read(fname):
    return open(local(fname)).read()

setup(
    name='lsh-filter',
    version='0.0.1',
    description='pure python near-duplicate document detection system',
    url='http://www.github.com/escherba/lsh-filter',
    author='Evan Rosen',
    author_email='rosen21@gmail.com',
    packages=find_packages(exclude=['tests', 'scripts']),
    entry_points={
        'console_scripts': [
            'lsh_filter = lsh_filter.lsh_app:main',
        ]
    },
    setup_requires=['nose>=1.0',
                    'coverage',
                    'nosexcover',
                    'mock'],
    install_requires=[],
    test_suite='nose.collector'
)
