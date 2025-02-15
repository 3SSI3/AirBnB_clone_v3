#!/usr/bin/python3
"""
Starts a Flask web application
"""
import storage from models
import app_views from api.v1.views
import Flask from flask
import jsonify from flask

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext

if __name__ = '__main__':
    host = getenv("HBNB_API_HOST") if
getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
