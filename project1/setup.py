
from setuptools import setup, find_packages

setup(
	name='Project1',
	version='1.0',
	author='Andrew Duffle',
	author_email='andrew.g.duffle-1@ou.edu',
	packages=find_packages(exclude=('tests','docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']
)
