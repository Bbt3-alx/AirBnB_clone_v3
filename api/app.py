#!/usr/bin/python3
"""Start the api"""


from flask import Flask
from models.engine import db_storage
from db_storage import DBStorage
from app.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def clone_storage(exception):
    """Clone the storage"""
    DBStorage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
