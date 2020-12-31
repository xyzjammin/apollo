from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_talisman import Talisman

# just added
#from SQLAlchemy import create_engine 
#from SQLAlchemy.orm import sessionmaker

# app instance
app = Flask(__name__)

# SSL / Content-Security-Policy
csp = {
  'default-src': [
    '\'self\'',
    'unsafe-inline',
    'https://www.fileundernda.com',
    'https://www.fileundernda.com',
    'www.fileundernda.com',
    'fileundernda.com'
    'https://ssl.gstatic.com',
    'data:',
    'gap:'
  ],
  'style-src': [
    '\'self\'',
    'unsafe-inline'
  ],
  'media-src': '*',
  'script-src': [
    '\'self\'',
    'unsafe-inline',
    'https://fileundernda.com',
    'https://www.fileundernda.com',
    'www.fileundernda.com',
    'fileundernda.com'
  ],
  'style-src': [
    '\'self\'',
    'unsafe-inline'
  ]
}

Talisman(app, content_security_policy=csp)


# app configuration
app.config.from_object(Config)

# database & migration handling
db = SQLAlchemy(app)
migrate = Migrate(app, db)

'''
engine = create_engine (
  app.config['SQLALCHEMY_DATABASE_URI'],
  pool_size=5,
  max_overflow=10,
  pool_timeout=1
)
'''

# must be at bottom to avoid circ refs
from app import routes, models

