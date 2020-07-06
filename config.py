import os
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.urandom(32)
# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://lindachen@localhost:5432/fyyur'
