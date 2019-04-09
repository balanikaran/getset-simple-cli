from setuptools import setup

setup(
    name='GetSetListen',
    version='1.0',
    author='Karan Balani',
    py_modules=['getset'],
    install_requires=[
        'Click', 'Requests'
    ],
    entry_points='''
        [console_scripts]
        getset=getset:cli
    ''',
)