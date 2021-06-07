import os

SECRET_KEY='d999ff38f5559f038cea840d0b77efd2e324f1e6'
SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI') or 'sqlite:///Site.db'
