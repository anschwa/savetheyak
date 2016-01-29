# -*- coding: utf-8 -*-
'''Management commands.'''

import os
import shutil

from flask.ext.script import Manager
from savetheyak.main import app, freezer

manager = Manager(app)
build_dir = app.config['FREEZER_DESTINATION']

HERE = os.path.dirname(os.path.abspath(__file__))

@manager.command
def install():
    '''Installs all required packages.'''
    os.system('pip install -U -r requirements.txt')

@manager.command
def build():
    """Builds the static files."""
    print("Freezing it up! Brr...")
    freezer.freeze()  # Freezes the project to build/
    print('...done')


@manager.command
def deploy(push=True):
    '''Deploys the site to GitHub Pages.'''
    build()
    print('Deploying to GitHub pages...')
    command = 'ghp-import -b gh-pages -m "[deploy] Build" '
    if push:
        command += '-p '
    command += build_dir
    os.system(command)
    print('...done')

if __name__ == '__main__':
    manager.run()
