try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A Donald Trump Twitter bot',
	'author': 'Tom Koker',
	'url': 'Url',
	'download_url': 'Download Url',
	'author_email': 'me@tomkoker.com',
	'version': '0.1',
	'install_requires': ['twitter'],
	'packages': ['trumpy'],
	'scripts': ['bin/trumpy'],
	'name': 'trumpy'
}

setup(**config)