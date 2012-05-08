# econding=utf8

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = 'django-elfinder',
    version = '0.2',
    description = 'Django connector for elFinder 2',
    long_description = README,
    author = 'Mike Ryan',
    author_email = 'mike@fadedink.co.uk',
    url = 'https://github.com/mikery/django-elfinder/',
    download_url = 'https://github.com/mikery/django-elfinder/tarball/v0.2',
    packages = find_packages(),
    include_package_data=True,
    requires = ['django (>=1.3)', 'mptt (>=0.5.2)'],
)