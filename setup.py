from setuptools import setup

setup(
    name='runforever',
    version='0.1.0',
    packages=['runforever'],
    entry_points={
        'console_scripts': [
            'runforever = runforever.__main__:main'
        ]
    })
