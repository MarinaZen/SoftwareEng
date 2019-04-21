import os


class Config:
    SECRET_KEY = 'c050e0f78c37cf44719375167b560343'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'se4g.assistance'
    MAIL_PASSWORD = '1234se4g'