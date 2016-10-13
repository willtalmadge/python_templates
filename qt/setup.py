from setuptools import setup

setup(
    name='qt_template',
    version='0.1.0',
    packages=[
        'qt_template'
    ],
    url='',
    license='',
    author='William Talmadge',
    author_email='william@rppl.com',
    description='This is my project description',
    entry_points={
        'console_scripts': ['qt_cmd = qt_template.bin.main:main']
    },
    test_suite='tests',
    include_package_data=True
)
