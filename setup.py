from setuptools import setup, find_packages

setup(
    name='rdcgen',
    version='0.1',
    py_modules=find_packages(),
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
