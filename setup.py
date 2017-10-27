from setuptools import setup, find_packages

setup(
    name='rdcgen',
    description='Generate RDCMan config files from Active Directory',
    author='John Frederick Cornish IV',
    licence='GPLv3',
    version='1.0',
    packages=['rdcgen'],
    install_requires=[
        'click',
        'ldap3',
        'PyYAML',
        'lxml',
    ],
    entry_points='''
    [console_scripts]
    rgen=rdcgen:cli
    ''',
)
