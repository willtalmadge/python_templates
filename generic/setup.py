from setuptools import setup

setup(
    name='my-project',
    version='0.1.0',
    packages=[
        'my_project'
    ],
    url='',
    license='',
    author='William Talmadge',
    author_email='william@rppl.com',
    description='This is my project description',
    entry_points={
        'console_scripts': ['my_cmd = bin.main:main']
    },
    test_suite='tests'
)
