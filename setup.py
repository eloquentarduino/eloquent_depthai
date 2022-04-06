import os.path
from distutils.core import setup
from glob import glob
from os.path import isdir


setup(
  name = 'eloquent_depthai',
  packages = ['eloquent_depthai'],
  version = '0.0.1',
  license='MIT',
  description = 'Eloquent interface to Luxonis DepthAI cameras',
  author = 'Eloquent Arduino',
  author_email = 'support@eloquentarduino.com',
  url = 'https://github.com/eloquentarduino/eloquent_depthai',
  download_url = 'https://github.com/eloquentarduino/eloquent_depthai/blob/master/dist/eloquent_depthai-0.0.1.tar.gz?raw=true',
  keywords = [
    'CV',
    'Computer Vision'
  ],
  install_requires=[
    'depthai',
  ],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
