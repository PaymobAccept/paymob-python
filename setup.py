#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='paymob',
      version='1.0.1',
      description='Your Paymob SDK in python',
      author='Paymob',
      author_email='maysragamal@paymob.com',
      url='https://github.com/PaymobAccept/paymob-python',
      packages=find_packages(exclude=["tests"]),
      install_requires=['requests']
     )
