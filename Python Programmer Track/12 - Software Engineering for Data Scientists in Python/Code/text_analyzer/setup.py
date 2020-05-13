# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:29:19 2020

@author: juanc
"""

# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='ggjuancamilo',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])
