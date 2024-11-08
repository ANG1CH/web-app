import os


class Config(object):
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', 'angich')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'lohotron')
    HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB = os.environ.get('POSTGRES_DB', 'project')

    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = '9kU4bP6KZtIPXGoiT7g25MzaaUjOFn2W18j7H7ad'
    SQLALCHEMY_TRACK_MODIFICATIONS = True