#!/usr/bin/env python


from setuptools import setup, find_packages

setup(
    name='crpk',
    py_modules=None,
    version="0.2",
    keywords=["Pakistani", "emergency", "services", "internet"],
    description="(C)ode (R)ed (P)a(k)istan.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-pkradio-220409.html',
        'Source': 'https://github.com/siphr/pkradio',
        'Tracker': 'https://github.com/siphr/pkradio/issues',
    },
    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['crpk'],
    package_data = {
        'crpk':['data/institutions.json']
        },
    platforms="any",
)
