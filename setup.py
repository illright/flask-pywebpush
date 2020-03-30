"""
Flask-pyWebPush
---------------

A clean interface to `pywebpush` from Flask. Basically, a very thin wrapper.
"""
import setuptools


with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name="Flask-pyWebPush",
    version="1.1",
    url="https://github.com/illright/flask-pywebpush",
    license="MIT",
    author="Lev Chelyadinov",
    author_email="leva181777@gmail.com",
    description="A clean interface to pywebpush from Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['flask_pywebpush'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pywebpush',
    ],
    python_requires=">= 3.6",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
