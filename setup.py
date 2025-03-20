from setuptools import setup, find_packages
from _version import __version__

#with open('requirements.txt') as f:
#    install_requires = f.read().splitlines()

setup(
  name='hm-ricing-mode',
  packages=find_packages(),
  version=__version__,
  author='mipmip',
  description='',
  #install_requires=install_requires,
  scripts=['_version.py'],
  py_modules=['hmrice'],
  entry_points={
    'console_scripts': ['hmrice = hmrice:main']
  },
)
