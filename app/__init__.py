from flask import Flask
import logging
import os
from logging.handlers import RotatingFileHandler 

from config import app_config


logger = None
config = None

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    # register configuration files
    app.config.from_object(app_config[config_name])
    # overrides if instance file exists
    # app.config.from_pyfile('config.py')
    # override any variables
    if 'WATCH_FOLDER' in os.environ:
        app.config['WATCH_FOLDER'] = os.environ['WATCH_FOLDER']
    print(app.config)
    global config
    config = app.config
    
    # add logging 
    handler = RotatingFileHandler(config_name + '.log', maxBytes=1000000, backupCount=10)
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    global logger
    logger = app.logger

    # add blueprint
    from app.api.routes import mod
    app.register_blueprint(mod, url_prefix='/api')
    
    return app