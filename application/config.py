import os


class Config:
    SECRET_KEY='248fb9a5bdffa13c0bc136504ebf75c2'
    SQLALCHEMY_DATABASE_URI='sqlite:///shop.db'
    
    # SQLALCHEMY_TRACK_MODIFICATIONS=True
    # MAIL_SERVER = 'mail.hossainfoysal.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USE_SSL = True
    # MAIL_USERNAME = os.getenv('EMAIL_USERNAME')
    # MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    # print(MAIL_USERNAME)
    # print(MAIL_PASSWORD)
    # MAIL_USERNAME = 'devops.tesla@gmail.com'
    # MAIL_PASSWORD = '#@(1JustLoveGamming.gmail)@#'