from setuptools import setup, find_packages

setup(
  name='optikmer',
  version='0.0',
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'optikmer = optikmer.optikmerjellyfish:main',
    ],
  },
  install_requires=[
    'matplotlib',
  ]

)