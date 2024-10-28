from setuptools import setup, find_packages

setup(
    name='kavi',
    version='0.1.0',
    author='Manjunatha',
    author_email='manjunath@infatoz.com',
    description='A Kannada programming language parser and interpreter',
    packages=find_packages(),
    install_requires=[
        'ply',  # Add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
