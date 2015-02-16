from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-ckandu',
    version=version,
    description="Theme for www.data.ug ckan",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Eve & Reinier',
    author_email='reinier.battenberg@mountbatten.net',
    url='www.data.ug',
    license='GPL 3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.ckandu'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        ckandutheme=ckanext.ckandu.plugin:CkanDuThemePlugin
        # Add plugins here, e.g.
        # myplugin=ckanext.ckandu.plugin:PluginClass
    ''',
)
