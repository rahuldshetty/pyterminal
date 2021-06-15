from setuptools import setup, find_packages

setup(
    name='pyterminal',
    version='0.0.1',
    url='https://github.com/rahuldshetty/pyterminal.git',
    author='Rahul D Shetty',
    author_email='35rahuldshetty@gmail.com',
    description='Launch terminal from your browser',
    packages=find_packages(include=['pyterminal', 'pyterminal.*']),    
    install_requires=open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': ['pyterminal=pyterminal.app:main']
    }
)