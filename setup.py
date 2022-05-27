try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Farm management game where the obejective is to make good'
    'decisions each year so the bank does not take the farm. Created in the '
    'process of working through Learn Python the Hard Way by Zed Shaw',
	'author': 'Laura Cathey Lubinski', 
	'author_email': 'cathlaura@gmail.com',
	'version': '0.1',
	'packages': ['FarmWisdom'],
	'scripts': [],
	'name': 'FarmWisdom'
}

setup(**config)