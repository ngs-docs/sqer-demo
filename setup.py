import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(name="sqer",
      version="0.1",
      packages=['sqer'],
      install_requires=["screed >= 0.7"],
      setup_requires=["nose >= 1.0"],
      scripts=["count-reads.py"],
      test_suite = 'nose.collector',
)
