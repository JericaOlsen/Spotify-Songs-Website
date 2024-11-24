from setuptools import setup


setup(
    name='mystatistics',
    version='0.2.0',
    author='Jerica Olsen',
    author_email='whatisacirej@gmail.com',
    packages=['mystatistics'],
    license='LICENSE.txt',
    description='A package that calculates mean median and mode',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    python_requires= '>=3.5,<4',
)

