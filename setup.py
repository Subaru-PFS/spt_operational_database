#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For ICS, try to get a setuptools which gives us the layout we want

try:
    import sdss3tools
    from sdss3tools import setup
except ImportError:
    from setuptools import setup

def main():
    setup(name='opdb',
          version='0.1',
          description='PFS operational database (opDB) tools',
          author='Kiyoto Yabe',
          url='https://github.com/Subaru-PFS/spt_operational_database',
          install_requires=['sqlalchemy', 'psycopg2-binary'],
          zip_safe=False,
          include_package_data=True,
          license='',
          package_dir={'': 'python'},
          packages=['opdb'],
          extras_require={
              'dev': [
                  'numpy',
                  'pandas',
                  'astropy',
                  'pytest',
                  'alembic',
                  'pylint',
              ],
          },
          )

if __name__ == '__main__':
    main()
