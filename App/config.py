import os

PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False
