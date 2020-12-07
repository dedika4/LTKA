from flask import Flask
from flask_bootstrap import Bootstrap
import serial

app = Flask(__name__)

from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
bootstrap = Bootstrap(app)

from app import routes,models
