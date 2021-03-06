from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='autoc',
      version="0.1",
      description='autoc is a package for data cleaning exploration and modelling in pandas',
      long_description=readme(),
      author=['Eric Fourrier'],
      author_email='ericfourrier0@gmail.com',
      license='MIT',
      url='https://github.com/ericfourrier/auto-cl',
      packages=find_packages(),
      test_suite='test',
      keywords=['cleaning', 'preprocessing', 'pandas'],
      install_requires=[
          'numpy>=1.7.0',
          'pandas>=0.15.0',
          'seaborn>=0.5',
          'scipy>=0.14']
      )
