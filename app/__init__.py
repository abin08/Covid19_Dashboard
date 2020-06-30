import logging
import os
from flask import Flask
from flask_cors import CORS


LOG_DIR = "logs"
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)


log_filename = os.path.join(LOG_DIR, 'app.log')
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
app.logger.info("App started...")


from app import routes