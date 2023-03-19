import os


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    URL_DB = "postgresql://localhost"
    DB_NAME = os.environ.get('DB_NAME')
    SQLALCHEMY_DATABASE_URI = "{}/{}".format(URL_DB, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print(SQLALCHEMY_DATABASE_URI)


config = {
    'development': DevelopmentConfig
}
