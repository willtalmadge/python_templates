from setuptools import setup

setup(
    name='my-experiment',
    version='0.1.0',
    packages=[
        'my_experiment'
    ],
    url='',
    license='',
    author='William Talmadge',
    author_email='william@rppl.com',
    description='This is an experiment',
    entry_points={
        'console_scripts': ['do_experiment = bin.main:main']
    },
    test_suite='tests'
)
