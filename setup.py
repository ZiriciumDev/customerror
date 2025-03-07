from setuptools import setup
from src.main import customerror, error, trye, checkerr
setup(name='customerror',
      version='1.0',
      description='a simple tool to make custom errors',
      url='',
      author='Ziricium',
      author_email='ziriciumdev@gmail.com',
      license='AND',
      packages=['src'],
      zip_safe=False,
      requires=['time'])