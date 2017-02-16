#!/usr/bin/python
from setuptools import setup

# to install type:
# python setup.py install --root=/
def readme():
    with open('README.rst') as f:
        return f.read()
setup (name='Tashaphyne', version='0.3.1',
      description='Tashaphyne Arabic Light Stemmer',
      long_description = readme(),      
      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://tashaphyne.sourceforge.net/',
      license='GPL',
      package_dir={'tashaphyne': 'tashaphyne',},
      packages=['tashaphyne'],
      include_package_data=True,
      install_requires=[ 'pyarabic',
      ],      
      package_data = {
        'tashaphyne': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Natural Language :: Arabic',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Linguistic',
          ],
    );

