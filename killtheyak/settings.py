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
FLATPAGES_EXTENSION = '.md'

BASE_URL = 'http://daschwa.github.io/killtheyak'
GITHUB_REPO = 'http://www.github.com/daschwa/killtheyak'
PAGES_REPO = 'http://www.github.com/daschwa/killtheyak-pages'
RAW_PAGES_PREFIX = "https://raw.github.com/daschwa/killtheyak-pages/master/"

# View site locally
FREEZER_RELATIVE_URLS = True
