from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ofxparse',
      version=version,
      description="Tools for working with the OFX (Open Financial Exchange) file format",
      long_description=open("./README", "r").read(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='ofx, Open Financial Exchange, file formats',
      author='Jerry Seutter',
      author_email='jseutter.ofxparse@gmail.com',
      url='http://github.com/jseutter/ofxparse/tree/master',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          "BeautifulSoup>=3.0",
      ],
      entry_points="""
      """,
      )