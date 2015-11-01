# -*- coding: utf-8 -*-
import os

try:
    # Assumes package is located in the same directory
    # where this file resides
    PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    PACKAGE_DIR = ""


def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(PACKAGE_DIR)
# Where to build static files to
FREEZER_DESTINATION = os.path.join(PROJECT_ROOT, 'build')
FREEZER_DESTINATION_IGNORE = ['*.coffee']
DEBUG = True
SECRET_KEY = 'shhhh'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'fenced_code', 'footnotes']
FLATPAGES_ROOT = os.path.join(PROJECT_ROOT, 'killtheyak-pages')
FLATPAGES_EXTENSION = '.markdown'

BASE_URL = 'http://daschwa.github.io/savetheyak'
GITHUB_REPO = 'http://www.github.com/daschwa/savetheyak'
PAGES_REPO = 'http://www.github.com/daschwa/savetheyak-pages'
RAW_PAGES_PREFIX = "https://raw.github.com/daschwa/savetheyak-pages/master/"

# View site locally
FREEZER_RELATIVE_URLS = True
