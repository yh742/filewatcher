import os
from app import create_app
from flask_cors import CORS

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)
CORS(app)

if __name__ == '__main__':
    app.run(threaded=True)