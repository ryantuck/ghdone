from setuptools import setup, find_packages

setup(
    name='ghdone',
    version='0.0.0.1',
    install_requires=[
        'arrow',
        'click',
        'requests',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ghdone = ghdone:cli',
        ],
    },
)
