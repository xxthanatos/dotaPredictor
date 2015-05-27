try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# copy data objects from dota2-api to src folder

# TODO FILL THIS OUT
config = {
    'description': 'Dota Predictor',
    'author': 'Colin Watson',
    #'url': 'URL to get it at.',
    #'download_url': 'Where to download it.',
    'author_email': 'cwatsonuf@gmail.com',
    'version': '0.1',
    'install_requires': ['scipy', 'numpy'],
    'packages': ['predictor'],
    'scripts': [],
    'name': 'dotaPredictor'
}

setup(**config)
