"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tg_tqdm',
    version='0.0.2',
    description='Extension for tqdm progressbar in Telegram',
    license='MPLv2.0, MIT Licences',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ermakovpetr/tg_tqdm',
    author='Petr Ermakov',
    author_email='ermakov.pd+github@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='progressbar progressmeter progress bar meter'
             ' rate eta console terminal time telegram',
    packages=['tg_tqdm'] + ['tg_tqdm.' + i for i in find_packages('tg_tqdm')],
    install_requires=['tqdm', 'telepot'],
    project_urls={
        'Source': 'https://github.com/ermakovpetr/tg_tqdm/',
    },
)