import os

from setuptools import setup, find_namespace_packages

__version__ = '0.0.2'

script_dir = os.path.dirname(os.path.realpath(__file__))
bin_dir = os.path.join(script_dir, 'dopltech', 'sdk', 'bin')

setup(
   name='dopltech-sdk',
   version=__version__,
   description='Dopl Technologies SDK',
   author='Ryan James',
   author_email='ryan@dopltechnologies.com',
   url='https://github.com/dopl-technologies/sdk-python',
   keywords=['dopl', 'technologies', 'telerobotics', 'sdk', 'electrophysiology', 'medicine'],
   packages=find_namespace_packages(include=['dopltech.*']),
   install_requires=['dopltech-api-protos', 'grpcio', 'grpcio-tools'],
   data_files=[('lib/site-packages', [bin_dir + '/libsdk.so'])],
)