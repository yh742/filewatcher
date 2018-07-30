from flask import Flask
import logging
from logging.handlers import RotatingFileHandler 

from config import app_config

logger = None

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    # register configuration files
    app.config.from_object(app_config[config_name])
    # overrides if instance file exists
    app.config.from_pyfile('config.py')
    print(app.config)
    
    # add logging 
    handler = RotatingFileHandler(config_name + '.log', maxBytes=1000000, backupCount=10)
    app.logger.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    global logger
    logger = app.logger

    #add blueprint

    from app.api.routes import mod
    #from app.site.routes import mod
    #from app.admin.routes import mod
    #app.register_blueprint(site.routes.mod)
    app.register_blueprint(mod, url_prefix='/api')
    #app.register_blueprint(admin.routes.mod, url_prefix='/admin')
    
    return app